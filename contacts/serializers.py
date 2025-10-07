from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'age', 'phone', 'country', 'company', 'created_at']

    def validate_age(self, value):
        if value < 18 or value > 120:
            raise serializers.ValidationError('Edad fuera de rango')
        return value

    def validate_country(self, value):
        if value not in ['honduras', 'nicaragua', 'guatemala']:
            raise serializers.ValidationError('País inválido')
        return value

    def validate_company(self, value):
        # Lista de empresas válidas
        valid_companies = [
            # Honduras
            'Empresa FinaciaPlus', 'Empresa Credifinancial', 'Empresa Banca Confiable',
            'Empresa Inpluso Financiero', 'Empresa Finactiva',
            # Nicaragua
            'Empresa Nicaragua',
            # Guatemala
            'Empresa Guatemala'
        ]
        if value and value not in valid_companies:
            raise serializers.ValidationError('Empresa no válida')
        return value