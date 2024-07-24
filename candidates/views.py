# candidates/views.py

from rest_framework import generics
from .models import Candidate
from .serializers import CandidateSerializer

class CandidateListView(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class CandidateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
