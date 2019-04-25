from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^showHtml/$', views.showHtml, name="showHtml"),
    url(r'^getAllData/$', views.getAllData, name="getAllData"),
    url(r'^addOneData/$', views.addOneData, name="addOneData"),
    url(r'^updateOneData/$', views.updateOneData, name="updateOneData"),
    url(r'^deleteData/$', views.deleteData, name="deleteData"),
]