from django.db import models

class Category(models.Model):
    name = models.CharField(name="category", verbose_name="Kategoriya")
# Create your models here.
class Todo(models.Model):
    task_name = models.CharField(verbose_name="Topshiriq",name="task", max_length=250)
    is_completed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    description = models.TextField(verbose_name="Tavsif")
