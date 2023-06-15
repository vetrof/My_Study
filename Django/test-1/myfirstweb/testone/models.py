from django.db import models

# Create your models here.


class TestRecord(models.Model):
    record = models.CharField(max_length=256)

    def __str__(self):
        return self.record
