from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.criar_funcionario, name='criar_funcionario'),
]
