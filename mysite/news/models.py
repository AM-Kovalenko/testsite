from django.db import models
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')                   #
    content = models.TextField(blank=True, verbose_name='Контент')                          #
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')    #
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')               #атрибуты (поля БД)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)#
    is_published = models.BooleanField(default=True, verbose_name='Опубликованно')          #
    #Создание связей
    category = models.ForeignKey('Category',on_delete=models.PROTECT, verbose_name='Категория')#'Category' в "", тк она определена позже

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'news_id': self.pk})



    # Вторичная модель
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


    #Первичная модель
class Category(models.Model):
    title = models.CharField(max_length=150,db_index=True, verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse('category',kwargs={'category_id':self.pk})

    # Строковое представление объектов
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']