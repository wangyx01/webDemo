from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^showHtml/$', views.showHtml, name="showHtml"),
    url(r'^getAllCity/$', views.getAllCity, name="getAllData"),
    url(r'^addCity/$', views.addCity, name="addCity"),
    url(r'^deleteCity/$', views.deleteCity, name="deleteCity"),
]
