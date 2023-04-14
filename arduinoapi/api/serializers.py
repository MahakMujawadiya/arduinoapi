from .models import Config
from rest_framework.serializers import serializer
class ConfigSerializer(serializer.ModelSerializer):
    class Meta:
        model=Config
        fields='__all__'