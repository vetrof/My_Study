from django.db import models

# Create your models here.


class StickyNotes(models.Model):
    head = models.CharField(max_length=30, default='запись')
    note = models.TextField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.head} {self.note:.20}... "
