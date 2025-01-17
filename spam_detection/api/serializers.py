from rest_framework import serializers
from .models import User, Contact, SpamReport

class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model =User
      fiels = ['id', 'username', 'phone_number','email']

class ContactSerializer(serializers.ModelSerializer):
   class Meta:
      model = Contact
      fiels = ['id', 'name', 'phone_number','email']

class SpamReportSerializer(serializers.ModelSerializer):
   class Meta:
      model = SpamReport
      fiels = ['id', 'username', 'reported_by']