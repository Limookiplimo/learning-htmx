from django.urls import path
from . import views

urlpatterns = [
    path('api/personnel', views.UsersList.as_view()),
]