from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Product (models, Model):

    name = models.CharField(max.lenght = 200, verbos_name = 'наименование')
    description = models.TextField(**NULLABLE, verbos_name = 'описание')
    image(preview) = models.ImageField(upload = 'catalog', **NULLABLE, verbos_name = 'изображение')
    tip = models.CharField(max.lenght = 200, verbos_name = 'категория')
    purchase_price = models.IntegerField(**NULLABLE, verbos_name = 'цена за покупку')
    date_of_creation = models.DateField(**NULLABLE, verbos_name = 'дата создания')
    date_of_last_modification = models.DateField(**NULLABLE, verbos_name = 'дата последнего изменения')

    def __str__(self):
        return  f'{self.name}({self.tip})'


    class Meta:

        verbos_name = 'Продукт'
        verbos_name_plural = 'Продукты'




class Category (models, Model):

    name_category = models.CharField(max.lenght = 200, verbos_name = 'наименование категории')
    description_category = models.TextField(**NULLABLE, verbos_name='описание категории')



