from django.contrib import admin

# Register your models here.
from .models import Customer
from .models import Devices
from .models import Bill
from .models import Bookappointments
from .models import DevicePrice
admin.site.register(Customer)
admin.site.register(Devices)
admin.site.register(Bill)
admin.site.register(Bookappointments)
admin.site.register(DevicePrice)