from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'register', views.RegisterUser)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.login),
    path('logout/', views.logout),
    path('search/', views.Search.as_view()),
    path('send/', views.Send.as_view()),
    path('accept/', views.Accept.as_view()),
    path('reject/', views.Reject.as_view()),
    path('list_friends/', views.ListFriends.as_view()),
    path('list_friend_requests/', views.ListFriendRequests.as_view()),
]