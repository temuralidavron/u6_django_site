from captcha.fields import CaptchaField
from django import forms
# from django.contrib.auth.models import User
from django.template.defaultfilters import first

from accounts.models import CustomUser


class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'email',
            'last_name',
            'phone_number',
            'password')


    # def save(self, commit=True):
    #     return CustomUser.objects.create(
    #         username=self.cleaned_data.get('username'),
    #         first_name=self.cleaned_data.get('first_name'),
    #         last_name=self.cleaned_data.get('last_name'),
    #         password=self.cleaned_data.get('password'),
    #     )



class LoginForm(forms.Form):
    username=forms.CharField(max_length=200)
    password=forms.CharField(max_length=100)
    captcha=CaptchaField()



class EmailChat(forms.Form):
    subject=forms.CharField()
    message=forms.CharField()
    to=forms.CharField()


class ForgetPasswordForm(forms.Form):
    username=forms.CharField(max_length=200)


class DoneForm(forms.Form):
    code=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)
    re_password=forms.CharField(max_length=100)






