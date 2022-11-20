from django.urls import path
from .views import ListUsers, CreateUsers, json

urlpatterns = [
    path('consultar/', ListUsers.as_view(), name='listusers'),
    path('consultar/json', json, name='json'),
    path('cadastrar/', CreateUsers.as_view(), name='createusers')
]