# Generated by Django 3.1.2 on 2021-06-20 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_profile_destination'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('quantity', models.IntegerField()),
                ('country', models.CharField(max_length=122)),
                ('city', models.CharField(max_length=122)),
                ('Dcountry', models.CharField(max_length=122)),
                ('Dcity', models.CharField(max_length=122)),
            ],
        ),
    ]
