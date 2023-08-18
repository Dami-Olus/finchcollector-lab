from django.db import models
import datetime
from django.urls import reverse
from datetime import date

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
    
)

class Tag(models.Model):
    name = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse('toys_details', kwargs={'pk': self.id})

# Create your models here.
class Finch(models.Model):
    species = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    spotted = models.IntegerField()
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return f'{self.species} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    
    def fed_for_today(self):
     return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
    

class Feeding(models.Model):
    date = models.DateField('Feeding Date', default=datetime.date.today)
    meal = models.CharField(max_length=1,
     choices=MEALS,
     default=MEALS[0][0]                       
    )

    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']


