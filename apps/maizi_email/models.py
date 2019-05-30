from django.db import models
from django.db import models

# Create your models here.
class EmailSend(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField('邮箱',max_length=50)