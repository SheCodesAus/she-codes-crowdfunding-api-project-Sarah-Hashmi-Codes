# Generated by Django 4.1.5 on 2023-02-22 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_goal_delete_projectimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledge',
            name='amount',
            field=models.FloatField(),
        ),
    ]
