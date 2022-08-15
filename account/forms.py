from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from account.models import Person


class SignUpForm(UserCreationForm):
    # username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)

    # password1 = forms.PasswordInput()
    # password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].help_text = None


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.PasswordInput()


class PersonalForm(forms.Form):

    SEX_CHOICE = [
        ('XY', 'Man'),
        ('YY', 'Woman')
    ]
    height = forms.IntegerField(required=True)
    weight = forms.IntegerField(required=True)
    age = forms.IntegerField(required=True)
    sex = forms.ChoiceField(choices=SEX_CHOICE, required=True)


# class PersonalForm(forms.ModelForm):
#
#     class Meta:
#         model = Person
#         exclude = ('user', )
