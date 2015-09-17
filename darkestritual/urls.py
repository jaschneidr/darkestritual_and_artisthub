"""

    darkestritual page URL conf

"""

from django.conf.urls import include, url
from django.contrib import admin

from home import views as home_views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home_views.global_home, name='index'),
    url(r'^music', home_views.global_music, name='music'),
    url(r'^visual', home_views.global_visual, name='visual'),
    url(r'^artisthub/', include('artisthub.urls')),
]
