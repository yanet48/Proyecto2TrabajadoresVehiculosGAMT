from django.db import models

class Company(models.Model):
  name = models.CharField(max_length=100)

  class Meta:
    db_table = "company"

