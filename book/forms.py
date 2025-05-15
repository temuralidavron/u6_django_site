from django import forms
from django.core.exceptions import ValidationError

from book.models import Author, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields=['full_name','birthday','isbn','country','email']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingiz'}),
            'birthday': forms.TextInput(attrs={'class': 'form-control','placeholder':'yosh' }),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),

        }


    def clean_birthday(self):
        birthday=self.cleaned_data.get('birthday')
        if birthday<18:
            raise forms.ValidationError("Yoshi 18 kichik bolishi mumkin emas")
        return birthday


    # def clean(self):
    #     birthday=self.cleaned_data.get('birthday')
    #     email=self.cleaned_data.get('email')
    #     if birthday>100:
    #         raise forms.ValidationError('ghjghkj')
    #     if email:
    #         raise forms.ValidationError




class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['author','title','description','price','image','file']