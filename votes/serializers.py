# votes/serializers.py
from rest_framework import serializers
from .models import Vote

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'user', 'candidate', 'created_at']
        read_only_fields = ['user', 'created_at']
