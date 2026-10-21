
from django.db import models


class Category(models.Model):
    name = models.CharField("Nazvaniye kategorii", max_length=100)

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategorii"

    def __str__(self):
        return self.name


class Book(models.Model):
    clientname = models.CharField("Nazvaniye", max_length=100)
    address = models.CharField("Address", max_length=100)
    clientphone = models.IntegerField("Telephone")

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Kniga"
        verbose_name_plural = "Knigi"

    def __str__(self):
        return self.clientname


class Order(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField("Kolichestvo", default=1)

    class Meta:
        verbose_name = "Zakaz"
        verbose_name_plural = "Zakazy"

    def __str__(self):
        return self.book.clientname
