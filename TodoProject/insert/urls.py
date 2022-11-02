from django.urls import path
from insert import views

urlpatterns = [
    path('add/', views.add),
    path('home/',views.home),
    path("delete/<int:tid>",views.delete)
]
