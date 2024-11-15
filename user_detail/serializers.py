from rest_framework import serializers,status
from user_detail.models import UserDetail



class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = '__all__'

