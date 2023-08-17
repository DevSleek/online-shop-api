from rest_framework.exceptions import ValidationError

from rest_framework import serializers
from ecommerce.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'image', 'price', 'description')

    @staticmethod
    def validate(data):
        name = data.get('name', None)
        price = data.get('price', None)

        if price < 1 or price > 999999999:
            raise ValidationError(
                {
                    'status': False,
                    'Message': 'Narx noto\'g\'ri kiritilgan!'
                }
            )

        if Product.objects.filter(name=name, price=price).exists():
            raise ValidationError(
                {
                    'status': False,
                    'Message': 'Mahsulotni nomi va narxi bir xil bo\'lgan mahsulotni saqlay olmisiz'
                }
            )

        return data
