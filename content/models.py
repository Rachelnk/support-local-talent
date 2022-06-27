from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
portfolio_type = [('Photography',('Photography')),
('Stylist ',('Stylist')),
('Makeup ',('Makeup')),
('Painting',('Painting')),
('Graphic designer',('Graphic designer')),
('Fashion designer',('Fashion designer')),
('Modeling',('Modeling')),
]
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User', null=True)
    username = models.CharField(max_length=60, verbose_name='Username', null=True)
    profile_pic = CloudinaryField('image')
    bio = models.TextField(max_length = 150, null = True, verbose_name= 'Bio')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created', null= True)
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated', null= True)

    def __str__(self):
        return str(self.id)
    
    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, username):
        return cls.objects.filter(user__username__icontains=username).all()
    
    def get_posts(self):
      return Portfolio.objects.filter(user=self).all()

    class Meta:
        verbose_name_plural = 'Profiles'

class Portfolio(models.Model):
    image = CloudinaryField('image', null=True)
    title = models.CharField(max_length=20, verbose_name='Title', null=True)
    description = models.CharField(max_length=500, verbose_name='Description', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', null = True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Profile', null =True)
    portfolio_type = models.CharField(choices=portfolio_type, max_length=150, null=True, verbose_name='Portfolio Category')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created', null= True)
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated', null= True)

    def __str__(self):
      return str(self.title)

    def save_portfolio(self):
        self.save()

    def delete_post(self):
        self.delete()

    # @classmethod
    # def search_post(cls, title):
    #     return cls.objects.filter(title__icontains=title).all()

    @classmethod
    def all_portfolio(cls):
        return cls.objects.all()

    # @classmethod
    # def filter_portfolio_types(cls, portfolio_type):
    #     portfolio_types = Portfolio.objects.filter(portfolio_type__icontains = portfolio_type)
    #     return portfolio_types
    
    class Meta:
        verbose_name_plural = 'Portfolios'
