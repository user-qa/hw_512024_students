# Generated by Django 5.0.4 on 2024-05-01 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_studentmodel_passport'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='updated_At',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
