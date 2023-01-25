from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

CATEGORIES =(
        ("Health", "Health"),
        ('Disaster Relief','Disaster Relief'), 
        ('Education',"Education")
    )
    
# class ProjectImages(models.Model):
#     project=models.ForeignKey(
#         'Project', 
#         on_delete=models.CASCADE, 
#         related_name='images')
#     images = models.FileField(upload_to='images',max_length=100,null=True)


class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    goal=models.FloatField() #use float for money
    image=models.URLField()
    is_open=models.BooleanField()
    date_created=models.DateTimeField(auto_now_add=True) #whenever project is created date will be recorded 
    owner=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="owner_projects"
     )
    category = models.CharField(max_length=200, null=True, choices= CATEGORIES )

    @property
    def pledged(self):
        return self.pledges.aggregate(sum=models.Sum('amount'))['sum']

class Pledge(models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,         #when project is cancelled all pledges will be cancelled too.
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )

