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


class PledgeDetailSerializer(PledgeSerializer):
    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        return instance

    

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
    raised = serializers.ReadOnlyField()
    

    def create(self,validated_data):    #method to creates and returns a new "Project", given the validated data.
        return Project.objects.create(**validated_data)
    
    # pledges = serializers.SerializerMethodField('get_pledges')

    # def get_pledges(selfself, obj):
    #     qset = Pledge.objects.filter(pledge__pk=obj.pk).order_by('amount')
    #     return PledgeSerializer(qset, many=True, read_only=True).data


class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance
