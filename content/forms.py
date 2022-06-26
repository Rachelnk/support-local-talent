from django import forms 
from django.contrib.auth.models import User
from content.models import Portfolio, Profile

portfolio_type = [('Photography',('Photography')),
('Stylist',('Stylist')),
('Makeup ',('Makeup')),
('Painting',('Painting')),
('Graphic designer',('Graphic designer')),
('Fashion designer',('Fashion designer')),
('Modeling',('Modeling')),
]

class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class UpdateProfileForm(forms.ModelForm):
    profile_image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['profile_image', 'bio']

class AddPortfolioform(forms.ModelForm):
    image = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    title = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
    description = forms.CharField(max_length=2200, required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Description'}))
    portfolio_type = forms.ChoiceField(choices=portfolio_type , required=True, widget=forms.Select(attrs={'class': 'form-control mb-4', 'placeholder':'Portfolio Type'}))   

    class Meta:
        model = Portfolio
        fields = ['image', 'title', 'description','portfolio_type',]