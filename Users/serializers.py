from rest_framework import serializers
from .models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["uid", "uname", "id", "password", "birthday", "phone", "profile_image", "email", "friends",
                  "personal_calender"]
