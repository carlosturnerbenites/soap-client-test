from django.conf.urls import url
from apps.series import views

urlpatterns = [
  url(r'^', views.index),
]
