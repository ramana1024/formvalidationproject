from django import forms
from.models import registrationdata

class registrationform(forms.Form):
    firstname=forms.CharField(
        label="enter first name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter First Name'
            }
        )
    )
    lastname = forms.CharField(
        label="enter last name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter last Name'
            }
        )
    )
    username = forms.CharField(
        label="enter username",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter UserName'
            }
        )
    )
    email = forms.EmailField(
        label="enter email",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email'
            }
        )
    )
    password1 = forms.CharField(
        label="enter password",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter password'
            }
        )
    )
    password2 = forms.CharField(
        label="confirm password",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'confirm password'
            }
        )
    )
    mobile= forms.IntegerField(
        label="enter Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Mobile Number'
            }
        )
    )
    def clean_username(self):
        username=self.cleaned_data.get('username')
        qs=registrationdata.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('username is already taken')
        elif len(username)<=5:
            raise forms.ValidationError('username must have more than 5 chars.')
        return  username

    def clean_email(self):
        email=self.cleaned_data.get('email')
        qs=registrationdata.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email is take already')
        elif not 'gmail.com' in email:
            raise forms.ValidationError('Email has to end with gmail.com.')
        return  email

    def clean_mobile(self):
        mobile=self.cleaned_data.get('mobile')
        qs=registrationdata.objects.filter(mobile=mobile)
        if qs.exists():
            raise forms.ValidationError('mobile numbuer is already taken')
        elif len(str(mobile))!=10:
            raise forms.ValidationError('Enter avlid Mobile Number')
        return  mobile

    def clea(self):
        data=self.cleaned_data
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')
        if password1!=password1:
            raise forms.ValidationError("password must match")
        elif len(password1)<=4 or len(password1)>=15:
            raise  forms.ValidationError("password length must be more then 4 chars or less than 15")
        return data






