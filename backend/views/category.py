from rest_framework import serializers, generics
   
from backend.models import Category
from backend.filters import IsOwnerFilterBackend

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'user', 'type', 'name', 'color', 'created_on', 'updated_on')

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (IsOwnerFilterBackend,)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (IsOwnerFilterBackend,)