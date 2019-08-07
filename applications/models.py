from django.db import models
from good.models import Good
from datetime import datetime
from user.models import User


class Application(models.Model):
    name = models.CharField(max_length=200)
    destination = models.CharField(max_length=150)
    date = models.DateTimeField(default=datetime.now(), auto_created=True)
    goods = models.ManyToManyField(Good)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
