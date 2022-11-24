from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=30)
    trash_name = models.CharField(max_length=30,null=True,blank=True)
    description = models.CharField(max_length=300,null=True,blank=True)
    trash_description = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    trash = models.ImageField(upload_to='trashes/',null=True,blank=True)
    target = models.ImageField(upload_to='target/',null=True,blank=True)
    sick = models.ImageField(upload_to='sick/',null=True,blank=True)
    sil = models.ImageField(upload_to='sil/',null=True,blank=True)
    latitude = models.FloatField(default=0.0,null=True,blank=True)
    longtitude = models.FloatField(default=0.0,null=True,blank=True)
    owners = models.ManyToManyField('accounts.User', related_name='animals',blank=True)
    
    def __str__(self):
        return self.name