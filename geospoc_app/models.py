from django.db import models
from django.core.validators import URLValidator
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True) # user ralationship OtO
    name = models.CharField(max_length=50)
    # email = models.EmailField(max_length=100, unique=True)
    web_address = models.TextField(validators=[URLValidator()], max_length=250)
    attachment = models.FileField(upload_to='documents/', blank=True)
    cover_letter = models.FileField(upload_to='Cover_letter/', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True)
    # IP address and Location
    ip_address = models.GenericIPAddressField(protocol='IPv4', null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    Rating_CHOICES = (
        (1, 'Poor'),
        (2, 'Average'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent')
    )
    rating = models.IntegerField(choices=Rating_CHOICES, default=1)
    Work_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No')
    )
    working = models.CharField(choices=Work_CHOICES, max_length=10, name="Do you like Working ?")

    def __str__(self):
        return self.name
