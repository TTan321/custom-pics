from django.db import models

class Profile(models.Model):
    firstname = models.CharField(max=256)
    lastname = models.CharField(max=256)
    email - models.EmailField()
    createdat = models.DateTimeField(auto_now_add=True)
    