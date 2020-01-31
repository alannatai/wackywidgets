from django.db import models

class Widget(models.Model):
  description = models.CharField(max_length=255)
  quantity = models.IntegerField()

  def __str__(self):
      return f"Description: {self.description} Quantity: {self.quantity}"
