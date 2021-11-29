from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import admin
from .models import User,Crypt,Cryptamount
class CryptInline(admin.StackedInline):
    model = Cryptamount
    extra = 3

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('email', 'username',)
        inlines = [CryptInline]


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('email', 'username',)
        inlines = [CryptInline]
