from django.contrib import admin
from .models import *

class TelegramSubscriberAdmin(admin.ModelAdmin):
    form = TelegramSubscriberForm
    list_display = ('chat_id', 'username', 'subscribed_at')
    list_display_links = ('chat_id', 'username')
    #так как передаем кортеж то для одного элемента надо поставить запятую
    search_fields = ('username',)
    list_filter = ('subscribed_at')

admin.site.register(TelegramSubscriber, TelegramSubscriberAdmin)