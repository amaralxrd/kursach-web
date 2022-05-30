from django.db import models
from simple_history.models import HistoricalRecords

class Coworking(models.Model):
    title = models.CharField( verbose_name='Название', max_length=100 )
    address = models.CharField( verbose_name='Место нахождения коворкинга', max_length=100, unique=True)
    work = models.CharField(verbose_name='В работе?',max_length=100)

    history = HistoricalRecords()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

class Tariffs(models.Model):
    title = models.CharField( verbose_name='Название тарифа', max_length=100)
    information = models.TextField(verbose_name='Информация о тарифе')
    price = models.IntegerField( verbose_name='Цена тарифа')
    hours = models.IntegerField(verbose_name='Времени в тарифе')

    history = HistoricalRecords()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

class Ticket(models.Model):
    coworking = models.ManyToManyField(Coworking, verbose_name='Выберите место')
    price = models.ManyToManyField(Tariffs, verbose_name='Тариф')
    name = models.CharField( verbose_name='ФИО', max_length=100)
    phone =  models.IntegerField(verbose_name='Номер телефона')

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'

