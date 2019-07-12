from django.db import models

# Create your models here.


class Entry(models.Model):
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    publish_date = models.DateTimeField('Дата публикации')
    title = models.CharField('Заголовок', max_length=255)
    url = models.URLField('Ссылка на новость')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

