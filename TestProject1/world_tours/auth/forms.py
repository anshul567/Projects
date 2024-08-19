from django import forms # type: ignore
from django.contrib.auth.models import User # type: ignore


class RegisterForm(forms.ModelForm):
    password=forms.CharField(lablel="Password", widget=forms.PasswordInput)
    comfirm_password=forms.CharField(lablel="Confirm Password", widget=forms.PasswordInput)


    class Meta:
        model=User
        fields=['username', 'password','confirm_password']

    def clean(self):
        cleaned_data=super().clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')

        if password and confirm_password and password!=confirm_password:
            raise forms.ValidationError("Password and Confirm Password does not match!")
            return cleaned_data
    
