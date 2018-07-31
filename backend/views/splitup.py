from rest_framework import serializers, generics

from backend.models import Splitup

class SplitupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Splitup
        fields = ('id', 'user', 'type', 'category', 'member', 'tag', 'budget', 'amount', 'description', 'created_on' , 'updated_on')

class SplitupList(generics.ListCreateAPIView):
    queryset = Splitup.objects.all()
    serializer_class = SplitupSerializer

class SplitupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Splitup.objects.all()
    serializer_class = SplitupSerializer