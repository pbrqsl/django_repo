from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView

# Create your views here.


def fav_links(request):
    return HttpResponse('aaa')

def fav_links_render(request):
    return render(request, 'links/links_manual.html', {
        'title': 'linki'
                                                       
    })

class ViewOne(TemplateView):
    template_name = 'links/links_manual.html'