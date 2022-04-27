from django.db import models


class DataModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(auto_now=True)
    data = models.JSONField(default=dict)
