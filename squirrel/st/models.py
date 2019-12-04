# st/models.py

from django.db import models

class Squirrel(models.Model):
    Latittude=models.FloatField()

    Longitude=models.FloatField()

    S_ID=models.CharField(
         max_length=20,
         primary_key = True,
    )    
  
    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = (
        (AM, 'AM'),
        (PM, 'PM'),
    )

    Shift=models.CharField(
        max_length = 2,
        choices = SHIFT_CHOICES,
        blank = True,
    )

    Date=models.DateField()
    
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    AGE_OTHER = ''

    AGE_CHOICES = (
        (ADULT, 'Adult'),
        (JUVENILE, 'Juvenile'),
        (AGE_OTHER, ''),
    )

    Age = models.CharField(
        max_length = 20,
        choices = AGE_CHOICES,
        default = AGE_OTHER,
        blank = True,
    )

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    FUR_OTHER = ''

    FUR_CHOICES = (
        (GRAY,'Gray'),
        (CINNAMON,'Cinnamon'),
        (BLACK,'Black'),
        (FUR_OTHER,''),
    )
    Fur=models.CharField(
        max_length = 10,
        choices = FUR_CHOICES,
        default = FUR_OTHER,
        blank = True,
    )

    ABOVE_GROUND = 'Above Ground'
    GROUND_PLANE = 'Ground Plane'
    LO_OTHER = ''

    LO_CHOICES =(
        (ABOVE_GROUND,'Above Ground'),
        (GROUND_PLANE,'Ground Plane'),
        (LO_OTHER,''),
    )

    Location = models.CharField(
        max_length = 20,
        choices = LO_CHOICES,
        default = LO_OTHER,
        blank = True,
    )

    S_location=models.CharField(max_length=200,blank=True,default='')

    Run = models.BooleanField()

    Chase = models.BooleanField()

    Climb = models.BooleanField()

    Eat = models.BooleanField()

    Forage = models.BooleanField()

    Other_a = models.CharField(max_length=200,blank=True,default='')

    Kuks = models.BooleanField()

    Quaas = models.BooleanField()

    Moans = models.BooleanField()

    T_flag = models.BooleanField()

    T_twitch = models.BooleanField()

    Approach = models.BooleanField()

    Indifferent = models.BooleanField()

    Run_from = models.BooleanField()
   
    def __str__(self):
        return self.S_ID


    
