from rest_framework import serializers

from .models import Store, Deal, ShoppingList


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = '__all__'


class DealSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Deal
        fields = '__all__'

    def get_image_url(self, obj):
        if obj.pic:
            request = self.context.get('request')
            image_url = obj.pic.file.url
            return request.build_absolute_uri(image_url)
        return None


class ShoppingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingList
        fields = '__all__'
