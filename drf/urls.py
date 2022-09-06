from django.contrib import admin
from django.urls import path, include
from book import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('category', views.CategoryGenericViewSet, basename='category')
router.register('book', views.BookGenericViewSet, basename='book')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
