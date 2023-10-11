from django.db import models


class Post(models.Model):
    tittle=models.CharField(max_length=25)
    desc=models.TextField(max_length=1000)
    publish_date=models.DateField()


