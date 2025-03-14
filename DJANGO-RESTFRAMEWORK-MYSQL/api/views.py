from rest_framework import viewsets
from .models import Company
from .serializer import CompanySerializer

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer