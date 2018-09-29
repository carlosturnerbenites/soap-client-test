from django.conf.urls import url
from django.urls import path
from apps.series import views

urlpatterns = [
  path('list/', views.series),
  path('create/', views.create),
  path('<int:id>/edit/', views.edit),

  path('store/', views.store),
  path('<int:id>/update/', views.update),
  path('<int:id>/delete/', views.delete),
]
