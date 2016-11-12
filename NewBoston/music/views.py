from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, DeleteView, UpdateView
from .models import Album


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'albums_list' # overrides default name 'object_list'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album  # what kind of album we create
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumEdit(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')
























# from django.http import HttpResponse
# from django.http import Http404
# from django.shortcuts import render, get_object_or_404
# from .models import Album, Song
#
# def index(request):
#     all_albums = Album.objects.all()
#     context = {'all_albums':all_albums}
#     return render(request, 'music/index.html', context)
#
# def detail(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     return render(request, 'music/detail.html', {'album':album})
#
# def favorite(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         selected_song  = album.song_set.get(pk=request.POST['song'])
#     except(KeyError, Song.DoesNotExist):
#         return render(request, 'music/detail.html',
#                       {'album': album,
#                        'error_message': 'You did not select a valid song.'
#                        })
#     else:
#         selected_song.is_favorite = True
#         selected_song.save()
#         return render(request, 'music/detail.html', {'album':album})

