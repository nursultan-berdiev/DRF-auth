from rest_framework.viewsets import ModelViewSet

from .models import Book, Category
from .serializers import CategorySerializer, BookSerializer


class CategoryGenericViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookGenericViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
