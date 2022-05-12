from django.urls import path, include

from Users import views
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    path('Users/', views.Users_list),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
