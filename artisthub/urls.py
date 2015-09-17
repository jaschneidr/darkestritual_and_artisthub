from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.artisthub_home, name='artisthub_home'),
    url(r'^(?P<artist_id>[0-9]+)/$', views.artist_profile, name='artist_profile'),
]