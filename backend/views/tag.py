from rest_framework import serializers, generics

from backend.models import Tag
from backend.filters import IsOwnerFilterBackend

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'user', 'name', 'created_on', 'updated_on')

class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = (IsOwnerFilterBackend,)

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = (IsOwnerFilterBackend,)