# Generated by Django 3.0.8 on 2020-07-19 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelpractice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='bio',
            field=models.CharField(default='Default bio', max_length=200),
        ),
    ]
