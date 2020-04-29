from django.urls import path
from MyAdmin.views import Form_View,Save,showforms,detailform
from django.contrib.auth import views as auth_views
from django.conf.urls import url
urlpatterns = [
url(r'^login/$', Form_View),
url(r'^save/$', Save),
url(r'^showform/$', showforms),
url(r'^detailform/$', detailform),
]

