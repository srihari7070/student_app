from django.conf.urls import url
from . import views
app_name='plo'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^registers/$', views.UserFormView.as_view(), name='registered'),
    url(r'^customer/add/$', views.SaveData.as_view(), name='saves'),
    url(r'^customer/about/$', views.About.as_view(), name='about'),
    url(r'^customer/ld/$', views.LoginDone.as_view(), name='login_done'),

]