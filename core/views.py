from rest_framework.viewsets import ModelViewSet

from core.models import Carro, Categoria, Marca
from core.serializers import CategoriaSerializer, MarcaSerializer, CarroSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer   

class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer     

# Create your views here.
