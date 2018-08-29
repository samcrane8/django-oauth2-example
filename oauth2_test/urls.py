"""oauth2_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^musics/$', views.MusicList.as_view (), name = 'music-list'),
    url (r'^music/(?P<pk>[0-9]+)/$', views.MusicDetail.as_view (), name =' music-detail'),

    url (r'^ albums/$', views.AlbumList.as_view ()),
    url (r'^album/(?P<pk>[0-9]+)/$', views.AlbumDetail.as_view ()),

    url (r'^bands/$', views.BandList.as_view ()),
    url (r'^band/(?P<pk>[0-9] +)/ $ ', views.BandDetail.as_view ()),

    url (r'^members/$', views.MemberList.as_view ()),
    url (r'^member/(?P<pk>[0-9]+)/$', views.MemberDetail.as_view ()),
]