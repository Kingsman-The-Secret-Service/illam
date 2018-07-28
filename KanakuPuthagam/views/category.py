from rest_framework import serializers, generics
from rest_framework_recursive.fields import RecursiveField
   
from KanakuPuthagam.models import Category

# class SubCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('name', 'parent')

class CategorySerializer(serializers.ModelSerializer):
    # parent = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    # children = SubCategorySerializer()
    # parent = RecursiveField(allow_null=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'parent', 'children', 'created_on', 'updated_on')
        depth = 9
    
    # def get_fields(self):
    #     fields = super().get_fields()
    #     fields['children'] = CategorySerializer(many=True)
    #     return fields



# class CategorySerializer(serializers.Serializer):
#     # parent = serializers.PrimaryKeyRelatedField(read_only=True)
#     # children = RecursiveField(allow_null=True)
#     # children = SubCategorySerializer()
#     name = models.CharField(max_length=255)
#     children = serializers.ListField(child=RecursiveField())

#     class Meta:
#         model = Category
#         fields = ('id', 'name', 'children', 'created_on', 'updated_on')
#         # fields = ('id', 'name', 'parent', 'children', 'created_on', 'updated_on')

#         # def get_related_field(self, model_field):
#         #     # Handles initializing the `subcategories` field
#         #     return CategorySerializer()

# # CategorySerializer.base_fields['children'] = CategorySerializer()

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
