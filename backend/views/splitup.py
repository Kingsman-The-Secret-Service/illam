from rest_framework import serializers, generics

from backend.models import Splitup
from backend.filters import IsOwnerFilterBackend

class SplitupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Splitup
        fields = ('id', 'user', 'budget', 'type', 'category', 'member', 'tag', 'amount', 'description', 'created_on' , 'updated_on')
        depth = 1

class SplitupList(generics.ListCreateAPIView):
    queryset = Splitup.objects.all()
    serializer_class = SplitupSerializer
    filter_backends = (IsOwnerFilterBackend,)

class SplitupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Splitup.objects.all()
    serializer_class = SplitupSerializer
    filter_backends = (IsOwnerFilterBackend,)