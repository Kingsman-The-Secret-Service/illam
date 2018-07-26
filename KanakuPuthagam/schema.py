from KanakuPuthagam.models import Member
import graphene
from graphene import Node
# from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

class MemberNode(DjangoObjectType):
    class Meta:
        model = Member
        # interfaces = (Node,)

class Query(graphene.ObjectType):
    members = graphene.List(MemberNode)

    def resolve_members(self, info):
        return Member.objects.all()

schema = graphene.Schema(query=Query)
