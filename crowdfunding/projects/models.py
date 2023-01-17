from django.db import models

CATEGORIES =(
        ("Health", "Health"),
        ('Disaster Relief','Disaster Releif'), 
        ('Education',"Education")
    )
    
class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    goal=models.IntegerField() #use float for money
    image=models.URLField()
    is_open=models.BooleanField()
    date_created=models.DateTimeField(auto_now_add=True) #whenever project is created date will be recorded 
    owner=models.CharField(max_length=200) #we have to change it to FK in future so he can be able to start a project
    category = models.CharField(max_length=200, null=True, choices= CATEGORIES )

class Pledge(models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,         #when project is cancelled all pledges will be cancelled too.
        related_name='pledges'
    )
    supporter = models.CharField(max_length=200)

