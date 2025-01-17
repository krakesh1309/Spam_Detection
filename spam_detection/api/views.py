from rest_framework import viewsets
from .models import User, Contact, SpamReport
from .serializers import UserSerializer, ContactSerializer, SpamReportSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from django.http import HttpResponse

def index(request):
   return HttpResponse("Welcome to the Sapm Detection API.")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'])
    def search_by_name(self, request):
        name_query = request.query_params.get('name', '')
        if not name_query:
            return Response({"detail": "Name query is required"}, status=status.HTTP_400_BAD_REQUEST)

        results = User.objects.filter(
            Q(username__startswith=name_query) |  # Assuming you want to search by username
            Q(username__icontains=name_query)
        ).order_by('username')

        serializer = self.get_serializer(results, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def search_by_phone(self, request):
        phone_query = request.query_params.get('phone_number', '')
        if not phone_query:
            return Response({"detail": "Phone number query is required"}, status=status.HTTP_400_BAD_REQUEST)

        results = User.objects.filter(phone_number=phone_query)
        if not results.exists():
            results = Contact.objects.filter(phone_number=phone_query)

        serializer = self.get_serializer(results, many=True)
        return Response(serializer.data)

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class SpamReportViewSet(viewsets.ModelViewSet):
    queryset = SpamReport.objects.all()
    serializer_class = SpamReportSerializer

    @action(detail=False, methods=['post'])
    def mark_as_spam(self, request):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({"detail": "Phone number is required"}, status=status.HTTP_400_BAD_REQUEST)

        spam_report = SpamReport.objects.create(
            phone_number=phone_number,
            reported_by=request.user
        )
        return Response({"detail": "Number marked as spam"}, status=status.HTTP_201_CREATED)
