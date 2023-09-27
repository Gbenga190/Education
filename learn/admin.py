from django.contrib import admin
from . models import user_profile, SubscribedUsers

# Register your models here.
admin.site.register(user_profile)

admin.site.register(SubscribedUsers)

class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_date')