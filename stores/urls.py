from django.urls import path

from .views import (
    StoreListCreate,
    StoreUpdate,
    DealListCreate,
    DealUpdate,
    ShoppingListListCreate,
    ShoppingListUpdate,

)


urlpatterns = [
    path('', StoreListCreate.as_view()),
    path('<int:pk>/', StoreUpdate.as_view()),
    path('deal/', DealListCreate.as_view()),
    path('deal/<int:pk>/', DealUpdate.as_view()),
    path('shopping_list/', ShoppingListListCreate.as_view()),
    path('shopping_list/<int:pk>/', ShoppingListUpdate.as_view()),

    ]
