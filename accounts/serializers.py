from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
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

