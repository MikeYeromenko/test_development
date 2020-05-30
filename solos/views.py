from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView

from solos.models import Solo


def index(request):
    context = {'solos': None}
    if request.GET.keys():
        solos = Solo.objects.all()
        if request.GET.get('instrument', None):
            solos = solos.filter(instrument=request.GET.get('instrument', None))
        if request.GET.get('artist', None):
            solos = solos.filter(artist=request.GET.get('artist', None))
        context['solos'] = solos
    return render(request, template_name='solos/index.html', context=context)


class SoloDetailView(DetailView):
    pass
