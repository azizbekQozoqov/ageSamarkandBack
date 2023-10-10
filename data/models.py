from django.contrib.gis.db import models


class BuildingType(models.Model):
    name = models.CharField(default='BUILDING', unique=True)
    def __str__(self):
        return self.name
    


# Create your models here.
class Building(models.Model):
    id = models.CharField(primary_key=True)
    year = models.IntegerField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    floors = models.IntegerField(default=1)
    type = models.ForeignKey(BuildingType, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/', blank=True)
    poly = models.PolygonField()
    def __str__(self) -> str:
        return f"<{self.id}: {self.address}>"
    