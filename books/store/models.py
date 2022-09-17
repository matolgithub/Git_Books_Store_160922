from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    author_name = models.CharField(max_length=255, default='Unknown author')

    def __str__(self):
        return f'ID: ---{self.name}, Name: ---{self.name}, Price: ---{self.price}, Author: ---{self.author_name}'
