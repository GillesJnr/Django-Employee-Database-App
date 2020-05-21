from django.urls import path
from . import views


urlpatterns = [
    path('', views.employee_form, name="home"),
    path('<int:id>/', views.employee_form, name="update"),
    path('list', views.employee_list, name="list"),
]