from django.contrib import admin
from django.urls import path
from .models import Product
from .views import ProductView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', ProductView)

urlpatterns = [
    # path("product/", admin.site.urls),
]

urlpatterns += router.urls
