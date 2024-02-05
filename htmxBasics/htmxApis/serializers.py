from rest_framework import serializers
from .models import Personnel

class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = ['first_name','last_name','age']