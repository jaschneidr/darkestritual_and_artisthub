from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render_to_response


def global_home(request):

    data = {}

    return render_to_response('index.html', data)


def global_music(request):

    data = {}

    return render_to_response('music.html', data)


def global_visual(request):

    data = {}

    return render_to_response('visual.html', data)