from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
portofolio_type = [('photography',('photography')),
('stylist',('stylist')),
('painting',('painting')),
('graphic designer',('graphic designer')),
('fashion designer',('fashion designer')),
('modeling',('modeling')),
('chemist',('chemist')),
]
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User', null=True)
    profile_pic = CloudinaryField('image')
    bio = models.TextField(max_length = 150, null = True, verbose_name= 'Bio')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created', null= True)
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated', null= True)

class Portfolio(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=20, verbose_name='Title', null=True)
    description = models.CharField(max_length=500, verbose_name='Description', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', null = True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Profile', null =True)
    category = models.CharField(choices=portofolio_type, max_length=150, null=True, verbose_name='Post Category')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created', null= True)
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated', null= True)
