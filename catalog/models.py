from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Product (models, Model):
    pass


class Category (models, Model):
    pass