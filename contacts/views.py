from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactSerializer
from .models import Contact
import logging

logger = logging.getLogger(__name__)

@api_view(['POST'])
@permission_classes([AllowAny])
def create_contact(request):
    """Crear un nuevo contacto"""
    try:
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()
            logger.info(f"Contacto creado: {contact.name} - {contact.country}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.warning(f"Datos inválidos: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.error(f"Error al crear contacto: {str(e)}")
        return Response(
            {'message': 'Error interno del servidor'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
@permission_classes([AllowAny])
def list_contacts(request):
    """Listar todos los contactos"""
    try:
        contacts = Contact.objects.all().order_by('-created_at')
        serializer = ContactSerializer(contacts, many=True)
        return Response({
            'count': contacts.count(),
            'contacts': serializer.data
        })
    except Exception as e:
        logger.error(f"Error al listar contactos: {str(e)}")
        return Response(
            {'message': 'Error al obtener contactos'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    """Verificar estado del API"""
    return Response({
        'status': 'OK',
        'message': 'API funcionando correctamente',
        'total_contacts': Contact.objects.count()
    })
