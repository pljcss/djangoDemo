from django.db import models
from edu_course.models import UserEmail


# Create your models here.
class EmailSend(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField('邮箱', max_length=50)

    to_user = models.ManyToManyField(UserEmail)

    class Meta:
        verbose_name = u"发送邮件"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name