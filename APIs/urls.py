from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'register', views.RegisterUser)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.login)
]