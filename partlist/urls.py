from django.urls import path

from . import views

urlpatterns = [
    path('', views.transaction_index, name='index'),
    #
    path('part_index', views.part_index, name='part_index'),
    path('part_add', views.part_add, name='part_add'),
    path('part_delete', views.part_delete, name='part_delete'),
    path('part_edit/<int:pk>', views.part_edit, name='part_edit'),
    path('part_detail/<int:pk>', views.part_detail, name='part_detail'),
    #
    path('transaction_index', views.transaction_index, name='transaction_index'),
    path('transaction_add', views.transaction_add, name='transaction_add'),
    path('transaction_delete', views.transaction_delete, name='transaction_delete'),
    path('transaction_edit/<int:pk>', views.transaction_edit, name='transaction_edit'),
]
