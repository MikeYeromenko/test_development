from django.http import HttpResponse
from django.shortcuts import render


from solos.models import Solo


def index(request):
    context = {'solos': Solo.objects.filter(instrument=request.GET.get('instrument', None))}
    return render(request, template_name='solos/index.html', context=context)
