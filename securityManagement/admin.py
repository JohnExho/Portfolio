from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("admin/css/custom_admin.css",)
        }