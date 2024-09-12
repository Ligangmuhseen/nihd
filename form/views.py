# Create your views here.
# views.py

from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer

from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import ContactForm


from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login

from datetime import datetime, timedelta  # Explicitly import datetime
import jwt
from django.conf import settings
from rest_framework import status
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser,JSONParser
from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework.views import APIView




class CsrfTokenView(APIView):
    def get(self, request):
        csrf_token = get_token(request)
        return Response({'csrf_token': csrf_token})
    



@api_view(['POST'])
def submit_form(request):
    if request.method == 'POST':
        form = ContactForm(request.data)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail(
                subject,
                f"Name: {name}\nEmail: {email}\nMessage: {message}",
                email,
                ['info@nihd.co.tz'],  # Replace with the recipient's Gmail address
                fail_silently=False,
            )
            return Response({'message': 'Form submitted successfully'})
        else:
            return Response({'message': 'Form data is not valid'}, status=400)








# @api_view(['POST'])
# def superuser_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.data)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)

#             if user is not None and user.is_superuser:
#                 login(request, user)

#                 token = generate_jwt_token(user)
#                 return Response({'message': 'Login successful'})
#             else:
#                 return Response({'message': 'Login failed'}, status=401)
#     else:
#         form = LoginForm()

    # return render(request, 'login_template.html', {'form': form})    





@api_view(['POST'])
def superuser_login(request):
    if request.method == 'POST':
        form = LoginForm(request.data)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Generate a JWT token
                token = generate_jwt_token(user)
                is_superuser = user.is_superuser
                is_active = user.is_active
                return Response({'message': 'Login successful', 'token': token, 'is_superuser': is_superuser, 'is_active': is_active})
            else:
                return Response({'message': 'Login failed'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            # Return validation errors
            return Response({'errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)
    else:
        form = LoginForm()
# Function to generate a JWT token
def generate_jwt_token(user):
    # Set the expiration time (e.g., 1 hour from now)
    expiration_time = datetime.utcnow() + timedelta(minutes=60)

    
    payload = {
        'user_id': user.id,
        'username': user.username,
        'is_superuser': user.is_superuser,
        'exp': expiration_time  # Add the expiration time to the payload
    }
    
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token




# views.py

# class ListUsersView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
   


# class CreateUserView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
  

# class UpdateUserView(generics.UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
 

   
         

# class DeleteUserView(generics.DestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
   


class UsersView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()

class UsersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
