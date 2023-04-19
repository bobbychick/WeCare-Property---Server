from django.contrib import admin
from .models import CustomUserModel

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email"]


admin.site.register(CustomUserModel, UserAdmin)
