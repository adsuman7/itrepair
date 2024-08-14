# urls.py

from django.urls import path
from .views import CustomerListCreateView, CustomerRetrieveUpdateDestroyView
# from .views import DeviceListCreateView, DeviceRetrieveUpdateDestroyView
from .views import BillListCreateView, BillRetrieveUpdateDestroyView
from .views import UserRegistration,CustomerRegistration
from .views import UserLogin,Deviceproblem,BookAppointment
from .views import DevicePriceListCreateView, DevicePriceRetrieveUpdateDestroyView
from .views import CombinedAppointmentCreateView,AppointmentsListView




urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyView.as_view(), name='customer-retrieve-update-destroy'),
    
    # path('devices/', DeviceListCreateView.as_view(), name='device-list-create'),
    # path('devices/<int:pk>/', DeviceRetrieveUpdateDestroyView.as_view(), name='device-retrieve-update-destroy'),

    path('bills/', BillListCreateView.as_view(), name='bill-list-create'),
    path('bills/<int:pk>/', BillRetrieveUpdateDestroyView.as_view(), name='bill-retrieve-update-destroy'),

    path('api/register/', UserRegistration.as_view(), name='register_user'),
    path('api/login/', UserLogin.as_view(), name='user-login'),

    path('api/deviceproblem/', Deviceproblem.as_view(), name='device-list'),
    path('api/deviceproblem/<int:pk>/', Deviceproblem.as_view(), name='device-detail'),

    path('api/bookappointment/', BookAppointment.as_view(), name='bookappointment-list'),

    path('api/device-prices/', DevicePriceListCreateView.as_view(), name='device-price-list-create'),
    path('api/device-prices/<int:pk>/', DevicePriceRetrieveUpdateDestroyView.as_view(), name='device-price-retrieve-update-destroy'),

    path('api/combined-appointments/', CombinedAppointmentCreateView.as_view(), name='combined-appointments-create'),
    
    path('api/appointments/', AppointmentsListView.as_view(), name='appointments-list'),
]
