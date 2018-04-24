from django.conf.urls import url
from . import views   
urlpatterns = [
  url(r'^amadon$', views.index),
  url(r'^process$', views.process),
  url(r'^amadon/checkout$', views.checkout),
  url(r'^logout$', views.logout)

]