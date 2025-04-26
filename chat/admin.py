from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ("role", "content", "timestamp")
    search_fields = ("content",)
    list_filter = ("role", "timestamp")
