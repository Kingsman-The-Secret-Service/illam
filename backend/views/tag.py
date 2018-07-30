from rest_framework import serializers, generics

from backend.models import Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'created_on', 'modified_on')

class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer