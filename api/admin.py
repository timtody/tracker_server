from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "summary"]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name"]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["id", "summary"]
