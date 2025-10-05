from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'age', 'phone', 'country', 'created_at']

    def validate_age(self, value):
        if value < 18 or value > 120:
            raise serializers.ValidationError('Edad fuera de rango')
        return value

    def validate_country(self, value):
        if value not in ['honduras', 'nicaragua', 'guatemala']:
            raise serializers.ValidationError('País inválido')
        return value