from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.core.exceptions import ValidationError


class UserRegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password', 'confirm_password')
        widgets = {'password': forms.PasswordInput}

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise ValidationError('Password cannot be empty.')
        password_validation.validate_password(password)
        return password

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if not confirm_password:
            raise ValidationError('Confirm your password.')
        if password != confirm_password:
            raise ValidationError('Passwords must be same.')
        return confirm_password

    def save(self, commit=True):
        user = super().save(False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserContinueRegisterForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name')
