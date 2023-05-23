from django.urls import path
from .views import employee_create

urlpatterns = [
    path('', employee_create, name='employee_create'),
]
