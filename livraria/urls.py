from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import CategoriaViewSet, MarcaViewSet, CarroViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'marca', MarcaViewSet)
router.register(r'carro', CarroViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
