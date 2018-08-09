from rest_framework import serializers, generics

from backend.models import Member
from backend.filters import IsOwnerFilterBackend

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'user', 'name', 'created_on', 'updated_on')

class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filter_backends = (IsOwnerFilterBackend,)

class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filter_backends = (IsOwnerFilterBackend,)