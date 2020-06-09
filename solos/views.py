from django.http import HttpResponse
from django.shortcuts import render


from solos.models import Solo


def index(request):
    context = {'solos': None}
    if request.GET.keys():
        solos_queryset = Solo.objects.all()
        if request.GET.get('instrument'):
            solos_queryset = solos_queryset.filter(instrument=request.GET['instrument'])
        artist_kwarg = request.GET.get('artist', None)
        if artist_kwarg:
            solos_queryset = solos_queryset.filter(artist=artist_kwarg)
        context = {
            'solos': solos_queryset,
        }
        if context['solos'].count() == 0 and artist_kwarg:
            context['solos'] = Solo.get_artist_tracks_from_musicbrainz(artist_kwarg)
    return render(request, template_name='solos/index.html', context=context)


# class SoloDetailView(DetailView):
#     model = Solo


def solo_detail(request, album, track, artist):
    context = {
        'solo': Solo.objects.get(slug=artist, track__slug=track, track__album__slug=album)
    }
    return render(request, 'solos/solo_detail.html', context)
