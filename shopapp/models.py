from django.db import models

class Shopview(models.Model):
	name=models.CharField(max_length=20)
	quantity=models.CharField(max_length=20)
	price=models.CharField(max_length=20)
