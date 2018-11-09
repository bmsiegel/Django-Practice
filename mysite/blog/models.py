from django.db import models

#classes are tables, each variable is a column, assign attributes to data

class Post(models.Model):
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
