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
from django.conf import settings
from django.core.paginator import Paginator
from django.contrib.sites.shortcuts import get_current_site


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
                                                       Q(user__email__icontains=query)).exclude(user__id=request.user.id).order_by('-user__last_login')

            try:
                page_number = request.GET['page']
            except KeyError:
                page_number = 1

            paginator = Paginator(matching_profiles, settings.PAGE_SIZE)
            page_obj = paginator.get_page(page_number)
            serializer = ProfileSerializer(page_obj.object_list, many=True)
            page_search_domain = f"http://{get_current_site(request)}/search/?page="

            if page_obj.has_previous():
                previous = page_search_domain + \
                    str(page_obj.previous_page_number())
            else:
                previous = page_search_domain + "1"

            if page_obj.has_next():
                next = page_search_domain + str(page_obj.next_page_number())
            else:
                next = page_search_domain + str(page_obj.paginator.num_pages)

            custom_response = {
                'current_page': page_obj.number,
                'previous': previous,
                'next': next,
                'result': serializer.data
            }

            return Response(custom_response)

        else:
            serializer = ProfileSerializer(matching_profile)
            return Response(serializer.data)
