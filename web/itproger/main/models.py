from django.db import models

# Create your models here.
class Articles(models.Model):
    name = models.CharField('Никнэйм', max_length=15)
    vol = models.FloatField('Алкоголь')
    non = models.FloatField('Другие напитки')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'участника'
        verbose_name_plural = 'Данные'