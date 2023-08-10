from rest_framework import serializers
from .models import feature 
class featureserializer (serializers.ModelSerializer):
    model=(feature),
    feilds=['id','username','email','University_name','country','DOG'],