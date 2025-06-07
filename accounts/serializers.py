from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework_gis.fields import GeometryField

from .models import CustomUser
User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    location = GeometryField(required=False, allow_null=True)
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = CustomUser
        fields = '__all__'

    def get_image_url(self, obj):
        if obj.pic:
            request = self.context.get('request')
            image_url = obj.pic.file.url
            return request.build_absolute_uri(image_url)
        return None


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords don't match.")
        return data


class ChangePasswordSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate(self, data):
        print(data)
        try:
            user = User.objects.get(id=data['user_id'])
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found.")

        if not user.check_password(data['current_password']):
            raise serializers.ValidationError({"current_password": "Current password is incorrect."})

        validate_password(data['new_password'], user)
        data['user'] = user  # pass user along
        return data

    def save(self, **kwargs):
        user = self.validated_data['user']
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user