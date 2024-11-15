from rest_framework import serializers,status
from rest_framework.response import Response
from rest_framework.views import APIView
from yebapp.models import UserDetail
from .models import GD,StdGD



class GdSerializer(serializers.ModelSerializer):
    class Meta:
        model = GD
        fields = '__all__'

class StdGDSerializer(serializers.ModelSerializer):
    user_marks = serializers.SerializerMethodField()

    class Meta:
        model = StdGD
        fields = ['gd_id','student_id','marks','user_marks']

    def get_user_marks(self,obj):
        user_detail = UserDetail.objects.filter(u_key=obj.student_id).first()
        return user_detail.marks if user_detail else None
    