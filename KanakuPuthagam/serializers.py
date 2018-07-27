from rest_framework import serializers

from KanakuPuthagam.models  import *

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'name','created_on','modified_on')

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ('id', 'source', 'created_on', 'modified_on')
