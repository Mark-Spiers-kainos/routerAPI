from django.db import models
from user.models import User

class Good(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
