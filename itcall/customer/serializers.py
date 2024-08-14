# serializers.py

from rest_framework import serializers
from .models import Customer, Devices, Bill,Bookappointments,DevicePrice
from django.contrib.auth.models import User
from .models import Appointments, Timeframe


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = ['brand', 'problem_kind', 'others', 'device_type']

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name','email']

class BookappointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookappointments
        fields = ['date', 'seven', 'eight', 'nine', 'ten', 'eleven', 'tweleve', 'thirteen', 'forteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

class DevicePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevicePrice
        fields = ['id', 'problem_kind', 'types', 'amount']



class TimeframeSerializer(serializers.Serializer):
    timeframes = serializers.ListField(child=serializers.CharField(), required=False)

class CombinedAppointmentSerializer(serializers.ModelSerializer):
    timeframes = TimeframeSerializer(required=False)

    class Meta:
        model = Appointments
        fields = ['date', 'devices', 'user', 'timeframes']

    def create(self, validated_data):
        timeframes_data = validated_data.pop('timeframes', {}).get('timeframes', [])

        # Create Appointments object
        appointment = Appointments.objects.create(**validated_data)

        # Create Timeframe object and associate it with the appointment
        Timeframe.objects.create(appointments=appointment, timeframes=timeframes_data)

        return appointment
class AppointmentsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = ['date', 'devices', 'user']


