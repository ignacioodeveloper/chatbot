from django.db import models




class ChatEntry(models.Model):


    
    user_message = models.TextField()
    reply = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.user_message, self.reply, self.timestamp    