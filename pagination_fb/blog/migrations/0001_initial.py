# Generated by Django 3.0.6 on 2023-04-17 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=25)),
                ('desc', models.TextField(max_length=1000)),
                ('publish_date', models.DateField()),
            ],
        ),
    ]