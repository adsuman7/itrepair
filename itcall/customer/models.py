from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
# Create your models here.
# models.py

from django.db import models

class Customer(models.Model):
    """Model representing a customer."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    # email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True, default='')
    address = models.TextField(blank=True, null=True,default='')
    city = models.TextField(blank=True, null=True,default='')
    state = models.TextField(blank=True, null=True,default='')
    zips = models.TextField(blank=True, null=True,default='')

    def __str__(self):
        return f"{self.user.username}"

class Device(models.Model):
    """Model representing a device (e.g., phone, laptop)."""
    TYPE_CHOICES = [
        ('mobile', 'Mobile'),
        ('pc', 'PC'),
        ('tablet', 'Tablet'),
    ]
    brand = models.CharField(max_length=100)
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    problem_kind = models.CharField(max_length=100, blank=True, null=True)  # New field for the type of problem
    others = models.CharField(max_length=100, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    device_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    def __str__(self):
        return f"{self.brand} Device"

class Bill(models.Model):
    """Model representing a bill for IT repair services."""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    issue_description = models.TextField()
    repair_notes = models.TextField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Bill #{self.id} - {self.customer.first_name} {self.customer.last_name} - {self.device.brand} Device - {self.device.problem_kind}"


class DevicePrice(models.Model):
    TYPE_CHOICES = [
        ('mobile', 'Mobile'),
        ('laptop', 'Laptop'),
        ('desktop', 'Desktop'),
        ('tablet', 'Tablet'),
    ]

    # device = models.ForeignKey(Device, on_delete=models.CASCADE)
    problem_kind = models.CharField(max_length=100, blank=True, null=True)
    types = models.CharField(max_length=10, choices=TYPE_CHOICES)
    brand=models.CharField(max_length=100, blank=True, null=True,default='others')
    amount = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.types} - ${self.amount}"

class Devices(models.Model):
    """Model representing a device (e.g., phone, laptop)."""
    TYPE_CHOICES = [
        ('mobile', 'Mobile'),
        ('pc', 'PC'),
        ('tablet', 'Tablet'),
    ]
    brand = models.CharField(max_length=100)
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    problem_kind = models.CharField(max_length=100, blank=True, null=True)  # New field for the type of problem
    others = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    def __str__(self):
        return f"{self.brand} Devices"
class BookAppointment(models.Model):
    date=models.DateField()
    devices=models.ForeignKey(Devices,on_delete=models.CASCADE)
    seven=models.BooleanField(default=True)
    eight=models.BooleanField(default=True)
    nine=models.BooleanField(default=True)
    ten=models.BooleanField(default=True)
    eleven=models.BooleanField(default=True)
    tweleve=models.BooleanField(default=True)
    thirteen=models.BooleanField(default=True)
    forteen=models.BooleanField(default=True)
    fifteen=models.BooleanField(default=True)
    sixteen=models.BooleanField(default=True)
    seventeen=models.BooleanField(default=True)
    eighteen=models.BooleanField(default=True)
    nineteen=models.BooleanField(default=True)
    def __str__(self):
        return f"{self.devices}"

class Bookappointments(models.Model):
    date=models.DateField()
    devices=models.ForeignKey(Devices,on_delete=models.CASCADE)
    seven=models.BooleanField(default=True)
    eight=models.BooleanField(default=True)
    nine=models.BooleanField(default=True)
    ten=models.BooleanField(default=True)
    eleven=models.BooleanField(default=True)
    tweleve=models.BooleanField(default=True)
    thirteen=models.BooleanField(default=True)
    forteen=models.BooleanField(default=True)
    fifteen=models.BooleanField(default=True)
    sixteen=models.BooleanField(default=True)
    seventeen=models.BooleanField(default=True)
    eighteen=models.BooleanField(default=True)
    nineteen=models.BooleanField(default=True)
    def __str__(self):
        return f"{self.devices}"

class Appointments(models.Model):
    date=models.DateField()
    devices=models.ForeignKey(Devices,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.date}"


class Timeframe(models.Model):
    SEVEN = '7:00 AM'
    EIGHT = '8:00 AM'
    NINE = '9:00 AM'
    TEN = '10:00 AM'
    ELEVEN = '11:00 AM'
    TWELVE = '12:00 PM'
    THIRTEEN = '1:00 PM'
    FOURTEEN = '2:00 PM'
    FIFTEEN = '3:00 PM'
    SIXTEEN = '4:00 PM'
    SEVENTEEN = '5:00 PM'

    TIME_CHOICES = [
        ("SEVEN", '7:00 AM'),
        ("EIGHT", '8:00 AM'),
        ("NINE", '9:00 AM'),
        ("TEN", '10:00 AM'),
        ("ELEVEN", '11:00 AM'),
        ("TWELVE", '12:00 PM'),
        ("THIRTEEN", '1:00 PM'),
        ("FOURTEEN", '2:00 PM'),
        ("FIFTEEN", '3:00 PM'),
        ("SIXTEEN", '4:00 PM'),
        ("SEVENTEEN", '5:00 PM'),
    ]
    appointments=models.ForeignKey(Appointments,on_delete=models.CASCADE)
    timeframes = models.CharField(max_length=10, choices=TIME_CHOICES)

    def __str__(self):
        return self.timeframe






