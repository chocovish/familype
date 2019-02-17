from rest_framework import serializers
from .models import User,Family



class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone','usertype','first_name','last_name','birthday','gender']
    
    def create(self, validated_data):
        return User.objects.create(setup_completed=True, username=validated_data['phone'], **validated_data)

class InviteMemberSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=10)

class MemberDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone','name','usertype','gender','setup_completed']