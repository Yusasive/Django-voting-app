from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Vote
from .serializers import VoteSerializer

class VoteCreateView(generics.ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
