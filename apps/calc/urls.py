from django.conf.urls import url
from django.urls import path
from apps.calc import views

urlpatterns = [
  path('', views.calc),
  path('op/', views.op),
]
