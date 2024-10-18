from django.db import models

# Create your models here.
class Rectangle(models.Model):
    length=models.IntegerField()
    width=models.IntegerField()
    def __iter__(self):
        yield {'length':self.length}
        yield {'width':self.width}