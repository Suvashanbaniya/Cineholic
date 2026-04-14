from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomuserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_verified', 'is_staff')
    list_editable = ('is_verified',)
    fieldsets = UserAdmin.fieldsets +(
        ('cineReview Extra',{'fields':('is_verified','title','bio','avatar')}),
    )
    

# Register your models here.
