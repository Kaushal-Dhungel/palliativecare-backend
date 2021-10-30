from rest_framework import serializers
from .models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"   

class ProfileSerializer(serializers.ModelSerializer):
    get_username = serializers.ReadOnlyField()
    get_email = serializers.ReadOnlyField()
    images = ImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Profile
        fields = "__all__"