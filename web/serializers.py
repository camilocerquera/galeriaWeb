__author__ = 'jc.cerquera10@uniandes.edu.co'
from web.models import Urls, Contact
from rest_framework import serializers

# Serializar modelo de URL
class UrlSerialializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Urls
        fields = ("id","url", "date", "user", "title", "description")

# Serializando modelo de Contacto
class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ("id", "name", "email", "msg", "date")