from django.conf.urls import url
from django.urls import path
from apps.series import views

urlpatterns = [
  path('list/', views.series),
  path('create/', views.create),
  path('edit/', views.edit),
  path('store/', views.store),
  path('update/', views.update),
  path('delete/', views.delete),
]
