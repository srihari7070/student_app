from django.conf.urls import url
from . import views

app_name='students'


urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^student/add/$',views.saveData.as_view(),name='saves'),
    url(r'student/(?P<pk>[0-9]+)/$', views.editData.as_view(), name="edit"),
    url(r'student/(?P<pk>[0-9]+)/delete/$', views.deleteData.as_view(), name="deletes"),
]