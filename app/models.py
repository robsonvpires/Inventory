from django.db import models

# Create your models here.
class Sala(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
	    return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
	    return self.name


class Item(models.Model):
	sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	name = models.CharField(max_length=255)
	quantity = models.IntegerField()

	def __str__(self):
		return self.name
