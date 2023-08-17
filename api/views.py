from rest_framework import viewsets
from product.models import Product
from .serializers import ProductSerializer

# Create your views here.
class ProductSerializerViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


