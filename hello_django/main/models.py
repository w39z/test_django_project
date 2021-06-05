from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField('Name', max_length=100)
    task = models.TextField('Definition')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class History(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField()
