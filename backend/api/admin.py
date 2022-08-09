from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('login', 'user_id')
    exclude = ('password',)


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)