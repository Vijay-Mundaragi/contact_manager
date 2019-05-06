from django.db import models
from django.utils.timezone import datetime

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    info = models.CharField(max_length=30)
    gender = models.CharField(max_length=50, choices=(
        ('male', 'Male'),
        ('feamle', 'Female')
    ))
    #blank=True to make that field optional
    image = models.ImageField(upload_to='images/', blank=True)
    
    #auto_add_now=True => set value to date when it was created
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
