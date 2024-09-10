from django.urls import path
from . import views


app_name = 'order'

urlpatterns = [
    path('create_order/<int:id_book>/', views.create_order, name='create_order'),
    path("orders_by_user_id/<int:user_id>/", views.orders_by_user_id, name="orders_by_user_id"),
    path('all_orders/', views.all_orders, name='list_orders'),
    path('order/<int:order_id>/', views.order_bel_by_id, name='order_bel_by_id'),
    path('order_close/<int:order_id>/', views.order_close_by_id, name='order_close_by_id'),
    path('edit/<int:order_id>/', views.edit_order_by_id, name='edit_order'),
]
