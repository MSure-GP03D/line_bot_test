# main/admin.py
from django.contrib import admin
from .models import User, ActionItem

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'line_user_id', 'created_at']
    search_fields = ['name', 'email']
    readonly_fields = ['firebase_uid', 'created_at']

@admin.register(ActionItem)
class ActionItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'assigned_to', 'due_date', 'completed', 'created_at']
    list_filter = ['completed', 'due_date', 'assigned_to']
    search_fields = ['title', 'description']
    date_hierarchy = 'due_date'