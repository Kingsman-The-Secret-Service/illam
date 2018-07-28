from rest_framework import serializers, generics

from KanakuPuthagam.models import Income

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ('id','date', 'name', 'source', 'amount', 'description', 'created_on' , 'modified_on')

class IncomeList(generics.ListCreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

class IncomeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer