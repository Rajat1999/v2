from django.db import models

# Create your models here.
class Hospitals(models.Model):
    name= models.CharField( max_length=200)
    address = models.TextField()
    files = models.FileField( upload_to='pdf/')
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    no_of_beds = models.IntegerField(null=True)


    def __str__(self):
        return self.name

