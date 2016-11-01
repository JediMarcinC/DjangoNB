from django.conf.urls import url
from . import views

app_name = 'music'  # not to be confused with 'detail' patterns in other possible apps.
                    # used in e.g. index.html > music:detail <

urlpatterns = [
    # music/
    url(r'^$', views.index, name='index'), # name is a variable that references this url pattern

    # music/<album_id>/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # music/<album_id>/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

]