from django.conf.urls import url
from . import views

app_name = 'music'  # not to be confused with 'detail' patterns in other possible apps.
                    # used in e.g. index.html > music:detail <

urlpatterns = [
    # music/
    url(r'^$', views.IndexView.as_view(), name='index'), # name is a variable that references this url pattern

    # music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # music/album/2/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumEdit.as_view(), name='album-edit'),

    # music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),







    # url(r'^(?P<album_id>[0-9]+)/$', views.DetailView.as_view(), name='detail'),








    # music/<album_id>/favorite
    # url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

]