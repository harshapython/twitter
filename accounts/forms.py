from django import forms
from .models import Tweets,Profile
from .models import Follow,comment,Replycomment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
#form for tweets 
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweets
        fields = ('text','profile_image',)
#form for signup
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required: Inform a valid email address.')
    def clean_email(self):
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']
    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2',)
# form for edit profile
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user','bio','birth_date','location','profile_image','header_image',)
        labels = {
            'user':(''),'bio':(''),'birth_date':(''),'location':(''),'profile_image':(''),'header_image':(''),
        }
#form for comments                  
class commentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('text','image',)
#form for reply comments
class replycommentForm(forms.ModelForm):
    class Meta:
        model = Replycomment
        fields = ('text','image',)

