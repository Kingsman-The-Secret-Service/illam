from rest_framework import serializers, generics

from backend.models import Budget
from backend.views.splitup import SplitupSerializer

class BudgetSerializer(serializers.ModelSerializer):
    splitup = SplitupSerializer(many=True, read_only=True)
    class Meta:
        model = Budget
        fields = ('id', 'user', 'name', 'start_date', 'end_date', 'splitup', 'created_on' , 'updated_on')

class BudgetList(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

class BudgetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer