from django.db import models


# Create your models here.

COLUMN_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
)
ROWS_CHOICES = (
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
    ("E", "E"),
)

class Booking(models.Model):
    numOfSeat = models.IntegerField()
    left = models.IntegerField(null = True)
    rows = models.CharField(max_length=1,choices=ROWS_CHOICES)
    column = models.CharField(max_length = 1,choices = COLUMN_CHOICES)
    
