from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import changevolume

def home(request):
    return render_to_response('sonoro.html', {
        'changed' : False,
        'current_volume': changevolume.get_volume(),
        }
    )

def set_volume(request, volume):
    changevolume.set_volume(int(volume))
    return HttpResponse(changevolume.get_volume())

def apple_crap(request):
    image_data = open("/home/aroman/telecomando/sonoro/static/apple-touch-icon.png", "rb").read()
    return HttpResponse(image_data, mimetype="image/png")
