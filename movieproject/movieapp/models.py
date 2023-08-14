from django.db import models
class Movie(models.Model):
    name=models.CharField(max_length=20)
    desc=models.CharField(max_length=20)
    year=models.IntegerField()
    img=models.ImageField(upload_to="gallery")
