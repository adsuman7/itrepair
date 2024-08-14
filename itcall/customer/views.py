from django.shortcuts import render
# Create your views here.
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAdminUser,AllowAny,BasePermission
from django.contrib.auth.hashers import make_password
# views.py
from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from rest_framework import exceptions
from rest_framework import generics
from .models import Customer
from .models import Bill
from .models import Bookappointments
from .models import Devices
from .models import Device,DevicePrice
from .serializers import BillSerializer
from .serializers import CustomerSerializer,DeviceSerializer,BookappointmentSerializer,DevicePriceSerializer
from .serializers import DeviceSerializer,AppointmentsListSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .models import Appointments, Timeframe
from .serializers import CombinedAppointmentSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import UserSerializer
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token


class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# class DeviceListCreateView(generics.ListCreateAPIView):
#     queryset = Device.objects.all()
#     serializer_class = DeviceSerializer

# class DeviceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Device.objects.all()
#     serializer_class = DeviceSerializer

class BillListCreateView(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class BillRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
class AllowAnyForPost(BasePermission):
    def has_permission(self, request, view):
        # Allow any user to register (POST) without authentication
        return request.method == 'POST'

class UserRegistration(APIView):
    authentication_classes = [TokenAuthentication]
    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAnyForPost()]
        return [IsAuthenticated()]

    def post(self, request, *args, **kwargs):
        # Allow any user to register (no authentication required for POST)
        # self.permission_classes = [AllowAny]
        self.check_permissions(request)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data.get('password')
            hashed_password = make_password(password)
            serializer.validated_data['password'] = hashed_password
            user = serializer.save()
            # Generate a token for the user
            token, created = Token.objects.get_or_create(user=user)
            # Include the token in the response
            return Response({'message': 'User registered successfully', 'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        # Only authenticated users can access this endpoint
        self.check_permissions(request)  # Explicitly check permissions for GET
        if request.user.is_staff:
            # Admin users can see the list of all users
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
        else:
            # Non-admin users can only see their own information
            user = request.user
            serializer = UserSerializer(user)

        return Response(serializer.data)
    def put(self, request, *args, **kwargs):
        self.check_permissions(request)
        user = self.request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            if 'password' in serializer.validated_data:
                # Hash the new password before saving
                password = serializer.validated_data['password']
                hashed_password = make_password(password)
                serializer.validated_data['password'] = hashed_password

            serializer.save()
            return Response({'message': 'User updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
class UserLogin(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        print(f"Token key: {token.key}")
        return Response({'token': token.key})

from rest_framework.permissions import AllowAny  # Import the AllowAny permission class

class CustomerRegistration(APIView):
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]  # Use AllowAny for the POST method
        return [IsAuthenticated()]

    def post(self, request, *args, **kwargs):
        self.check_permissions(request)
        serializer = CustomerSerializer(data=request.data)
        user=request.user
        print(user)
        if serializer.is_valid():
            user = serializer.save(user=request.user)
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        self.check_permissions(request)
        if request.user.is_staff:
            customers = Customer.objects.all()
            serializer = CustomerSerializer(customers, many=True)
        else:
            try:
                customer = request.user.customer
                serializer = CustomerSerializer(customer)
            except Customer.DoesNotExist:
                return Response({'message': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        self.check_permissions(request)
        try:
            customer = request.user.customer
        except Customer.DoesNotExist:
            return Response({'message': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Customer updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Deviceproblem(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            device = Devices.objects.get(pk=pk, user=self.request.user)
            return device
        except Devices.DoesNotExist:
            raise exceptions.NotFound(detail='Device not found or does not belong to the authenticated user.')

    def post(self,request,*args,**kwargs):
        serializer=DeviceSerializer(data=request.data)
        users=request.user
        print(users)
        if serializer.is_valid():
            device=serializer.save(user=users)   
            return Response({'message': "device update successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,*args,**kwargs):
        if request.user.is_staff:
            device=Devices.objects.all()
            serializer=DeviceSerializer(device,many=True)
        else:
            try:
                device=request.user.devices.all()
                serializer=DeviceSerializer(device,many=True)
            except Devices.DoesNotExist:
                return Response({'message': 'Devices not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        device = self.get_object(pk)
        serializer = DeviceSerializer(device, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': f"Device with ID {pk} updated successfully"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookAppointment(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = BookappointmentSerializer(data=request.data, context={'devices': request.user.devices})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Your appointment is booked. Check your email."}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            bookappointment = Bookappointments.objects.all()  # Assuming you have a BookAppointment model
            if not bookappointment:
                return Response({'message': 'No book appointments found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = BookappointmentSerializer(bookappointment, many=True)
        else:
            bookappointment = request.user.devices.bookappointments.all()
            if not bookappointment:
                return Response({'message': 'No book appointments found for the user'}, status=status.HTTP_404_NOT_FOUND)
            serializer = BookappointmentSerializer(bookappointment, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class DevicePriceListCreateView(generics.ListCreateAPIView):
    queryset = DevicePrice.objects.all()
    serializer_class = DevicePriceSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method == 'POST':  # If the request is for creating a new device price
            return [permissions.IsAdminUser()]  # Allow only admin users to create
        return super().get_permissions()  # For other HTTP methods, use the default permissions


class DevicePriceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DevicePrice.objects.all()
    serializer_class = DevicePriceSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]



class CombinedAppointmentCreateView(generics.CreateAPIView):
    serializer_class = CombinedAppointmentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class AppointmentsListView(generics.ListAPIView):
    serializer_class = AppointmentsListSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filter appointments based on the currently logged-in user
        user = self.request.user
        return Appointments.objects.filter(user=user)

    







        


            







