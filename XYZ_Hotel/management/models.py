from django.db import models
from django.db.models import DecimalField

# Create your models here.

class Record(models.Model):
    Occupant_Name = models.CharField(max_length = 300, null = False, help_text = "your name, surname first")
    Occupant_Email = models.EmailField()
    Occupant_Occupation =models.CharField(max_length = 200) 
    Amount_Paid = models.DecimalField(max_digits=10, decimal_places=2)
    Room_Number = models.IntegerField()
    No_of_Night = models.IntegerField()
    Start_date = models.DateTimeField()
    End_date = models.DateTimeField()
    
    def __str__(self):
        return self.Occupant_Name