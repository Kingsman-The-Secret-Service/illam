from rest_framework import serializers, generics

from backend.models import Budget
from backend.filters import IsOwnerFilterBackend
from backend.views.splitup import SplitupSerializer

class BudgetSerializer(serializers.ModelSerializer):
    splitup = SplitupSerializer(many=True, read_only=True)
    class Meta:
        model = Budget
        fields = ('id', 'user', 'name', 'start_date', 'end_date', 'description', 'splitup', 'created_on' , 'updated_on')

class BudgetList(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    filter_backends = (IsOwnerFilterBackend,)

    def get_queryset(self):
            return Budget.objects.all().filter(
                start_date__gte = self.request.session['startDate'],
                end_date__lte = self.request.session['endDate']
            )

class BudgetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    filter_backends = (IsOwnerFilterBackend,)