from django.db import models

# Create your models here.
class ChatEntry(models.Model):
    user_message = models.TextField()
    reply = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)