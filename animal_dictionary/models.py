from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/',null=True)
    trash = models.ImageField(upload_to='trashes/',null=True)
    target = models.ImageField(upload_to='target/',null=True)
    sick = models.ImageField(upload_to='sick/',null=True)
    sil = models.ImageField(upload_to='sil/',null=True)
    latitude = models.FloatField(default=0.0)
    longtitude = models.FloatField(default=0.0)
    owners = models.ManyToManyField('accounts.User', related_name='animals')
    
    def __str__(self):
        return self.name