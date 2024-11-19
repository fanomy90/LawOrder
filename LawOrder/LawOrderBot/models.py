from django.db import models

class TelegramSubscriber(models.Model):
    #данные пользователя
    chat_id = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.username} ({self.chat_id})'

    class Meta:
        verbose_name = 'Подписчик Telegram'
        verbose_name_plural = 'Подписчики Telegram'
        ordering = ['subscribed_at']