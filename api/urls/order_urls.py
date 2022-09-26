from django.urls import path
from api.views.order_views import (addOrderItems,getOrderById,
getMyOrders,getOrders,updateOrderToDelivered,updateOrderToPaid)

urlpatterns = [
    path('', getOrders, name='orders'),
    path('add/', addOrderItems, name='orders-add'),
    path('myorders/', getMyOrders, name='myorders'),
    path('<str:pk>/deliver/',updateOrderToDelivered, name='order-delivered'),
    path('order/<str:pk>/', getOrderById, name='user-order'),
    path('<str:pk>/pay/',updateOrderToPaid, name='pay'),
]