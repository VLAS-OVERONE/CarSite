from django.db import models

class Vehicle(models.Model):
    title = models.CharField('Марка Автомобиля', max_length=30)
    description = models.TextField('Описание автомобиля')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'