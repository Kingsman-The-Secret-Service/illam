from rest_framework import serializers, generics
   
from backend.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'user', 'date', 'type', 'category', 'member', 'tag', 'amount', 'description', 'created_on' , 'updated_on')
        depth = 1

class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer