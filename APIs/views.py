from rest_framework.viewsets import ModelViewSet
from .models import User, Profile
from .serializers import ProfileSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib import auth
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class RegisterUser(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    http_method_names = ['post',]


@api_view(['POST',])
def login(request):
    user = auth.authenticate(
        username=request.data['email'], password=request.data['password'])
    
    if user:
        auth.login(request, user)
        return Response({'Status': 'Success', "Message": "You have successfully Logged In!"}, status=status.HTTP_200_OK)

    return Response({'Status': 'Failed', "Message": "Invalid Credentials!"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET',])
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return Response({'Status': 'Success', "Message": "You have successfully Logged Out!"}, status=status.HTTP_200_OK)

    else:
        return Response({'Status': 'Failed', "Message": "You are not Logged In!"}, status=status.HTTP_404_NOT_FOUND)


class Search(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            query = request.data['q']
        except KeyError:
            return Response({'Status': 'Failed', "Message": "No query provided!"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            matching_profile = Profile.objects.get(user__email=query)
        except Profile.DoesNotExist:
            matching_profiles = Profile.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) |
                                                       Q(user__email__icontains=query))
            serializer = ProfileSerializer(matching_profiles, many=True)

        else:
            serializer = ProfileSerializer(matching_profile)
        return Response(serializer.data)
    


