from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100,help_text='A valid Email is Required')


    class Meta:
        model = Account
        fields = ("email","username","full_name","password1","password2","image")



class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid login")

class AccountUpdateForm(forms.ModelForm):

	class Meta:
		model = Account
		fields = ('email', 'username','image' )

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
		except Account.DoesNotExist:
			return email
		raise forms.ValidationError('Email "%s" is already in use.' % account)


	def image(self):
		image = self.cleaned_data['image']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(image=image)
		except Account.DoesNotExist:
			return image
		raise forms.ValidationError('image "%s" is already in use.' % account)


	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
		except Account.DoesNotExist:
			return username
		raise forms.ValidationError('Username "%s" is already in use.' % username)
