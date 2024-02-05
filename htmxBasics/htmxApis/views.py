from .serializers import PersonnelSerializer
from rest_framework import generics
from .models import Personnel


# Create your views here.
class UsersList(generics.ListAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer