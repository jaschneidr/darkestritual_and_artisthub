from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render_to_response


def artisthub_home(request):

    data = {}

    return render_to_response('artisthub_home.html', data)


def artist_profile(request, artist_id):

    data = {}

    return render_to_response('artist_profile.html', data)