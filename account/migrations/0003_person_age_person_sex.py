# Generated by Django 4.0.6 on 2022-08-14 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_person_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='sex',
            field=models.CharField(choices=[('XY', 'Man'), ('YY', 'Woman')], default='XY', max_length=10),
        ),
    ]
