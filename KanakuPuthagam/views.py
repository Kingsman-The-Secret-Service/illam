from KanakuPuthagam.models import Member
from KanakuPuthagam.serializers import MemberSerializer
from rest_framework import generics

class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer