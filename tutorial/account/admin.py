from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Crypt,Cryptamount
from .models import User,Crypt
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
class CryptInline(admin.StackedInline):
    model = Cryptamount
    extra = 2
class UserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username','email', ]
    inlines = [CryptInline]



admin.site.register(User, UserAdmin)
admin.site.register(Crypt)