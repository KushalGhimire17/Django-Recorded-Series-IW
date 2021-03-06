# Generated by Django 3.0.8 on 2020-07-19 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelrelation', '0003_auto_20200719_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='userdetail',
            name='country',
            field=models.ManyToManyField(to='modelrelation.Country'),
        ),
    ]
