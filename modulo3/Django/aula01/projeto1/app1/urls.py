from django.urls import path
from .views import index, create, modify

urlpatterns = [
    path('', index, name='index'),
    path('user/create', create, name='create'),
    path('user/modify/<int:user_id>', modify, name='modify')
]