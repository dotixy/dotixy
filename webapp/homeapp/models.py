# models.py
from django.db import models

class Drawing(models.Model):
    # a model of a drawing saved by the user
    # store the drawing data as a base64 string
    data = models.TextField()
