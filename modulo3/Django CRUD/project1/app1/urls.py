from django.urls import path
from .views import index ,create, modify, delete, calculo

urlpatterns = [
    path('', index, name='index'),
    path('test/calculo', calculo, name='calculo'),
    path('user/create', create, name='createuser'),
    path('user/modify/<int:user_id>', modify, name='modificar'),
    path('user/delete/<int:user_id>', delete, name='deleteuser')
]