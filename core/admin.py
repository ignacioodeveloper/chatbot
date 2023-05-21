from django.contrib import admin
from .models import ChatEntry
# Register your models here.
@admin.register(ChatEntry)
class ChatEntryAdmin(admin.ModelAdmin):
    list_display = ('user_message', 'reply', 'timestamp')