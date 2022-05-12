from rest_framework import serializers
from .models import Calenders


class CalendersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calenders
        fields = ["cid", "ccontent", "cclass"]
