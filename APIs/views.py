from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib import auth
# Create your views here.
class RegisterUser(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    http_method_names = ['post',]

@api_view(['POST',])
def login(request):
    print(request.data)
    user = auth.authenticate(username=request.data['email'], password=request.data['password'])
    if user:
        auth.login(request, user)
        return Response({'Status': 'Success', "Message": "You have successfully Logged In!"}, status=status.HTTP_200_OK)
    
    return Response({'Status': 'Failed', "Message": "Invalid Credentials!"}, status=status.HTTP_401_UNAUTHORIZED)