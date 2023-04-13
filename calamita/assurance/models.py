from django.db import models


class Node(models.Model):

    public_key = models.CharField(max_length=500)
    host = models.CharField(max_length=100)
