from rest_framework import serializers
from .models import Messages


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ["mid", "mcontent", "send_time"]
