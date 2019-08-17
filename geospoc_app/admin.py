from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.models import Group


# Register your models here.

from .models import UserProfile


admin.site.register(UserProfile)
admin.site.unregister(Group)