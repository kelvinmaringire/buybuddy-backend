from rest_framework import generics

from .models import Store, Deal, ShoppingList
from .serializers import StoreSerializer, DealSerializer, ShoppingListSerializer


class StoreListCreate(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class StoreUpdate(generics.RetrieveUpdateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class DealListCreate(generics.ListCreateAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer


class DealUpdate(generics.RetrieveUpdateAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer


class ShoppingListListCreate(generics.ListCreateAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer


class ShoppingListUpdate(generics.RetrieveUpdateAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
