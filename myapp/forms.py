from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django_recaptcha.fields import ReCaptchaField
from jobpostapp.models import job,post



class userform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    captcha = ReCaptchaField()
    


class app(forms.ModelForm):
    class Meta:
        model = job
        fields = "__all__" 



class Postss(forms.ModelForm):
    class Meta:
        model = post
        fields = "__all__"  