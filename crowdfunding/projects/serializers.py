from rest_framework import serializers
from .models import Project,Pledge, CATEGORIES


# class PledgeSerializer(serializers.Serializer):
    # id = serializers.ReadOnlyField()
    # amount = serializers.DecimalField(max_digits=20, decimal_places=2)
    # comment = serializers.CharField(max_length=200)
    # anonymous = serializers.BooleanField()
    # supporter = serializers.CharField(max_length=200)
    # project_id = serializers.IntegerField()
    
class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']
        read_only_fields = ['id', 'supporter']

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

# class CategorySerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField(read_only=True)
    owner = serializers.ReadOnlyField(source="owner.id")
    category = serializers.ChoiceField(CATEGORIES)
    

    def create(self,validated_data):    #method to create instance
        return Project.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
