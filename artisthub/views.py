from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from forms import SignupForm, ProfileForm

from models import *


def artisthub_home(request):

    if request.user.is_authenticated():
        user= request.user

        data = {
            'user': user,
        }

        return render_to_response('artist_home.html', data)

    else:
        data = {

        }
        return render_to_response('artisthub_home.html', data)


def artist_profile(request, artist_id):

    user = request.user
    artist = UserProfile.objects.get(id=artist_id)

    data = {
        'user': user,
        'artist': artist,
    }

    return render_to_response('artist_profile.html', data)


def user_signup(request):

    user = request.user

    # if user.is_authenticated():
    #    return artisthub_home(request)

    form = SignupForm(request.POST)

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('passwprd')
        confirm_password = request.POST.get('confirm_password')
        profile_type = request.POST.get('profile_type')
        email = request.POST.get('email')

        error = None

        if form.is_valid() and password == confirm_password:
            new_user = User.objects.create(username=username, email=email)
            new_user.set_password(password)
            new_user.save()

            up = UserProfile.objects.create(user=new_user, profile_type=profile_type)
            up.save()

            user = authenticate(username=new_user.username, password=password)
            login(request, user)

            data = {
                'profile': up,
                'user': new_user,
            }

        elif password != confirm_password:
            error = "Passwords did not match."

        elif not form.is_valid():
            error = "Please enter all required fields."

        if error:
            data = {
                'error': error,
                'form': form,
            }

            return render_to_response('forms/signup_form.html', data)

        return edit_profile_form(request)

    data = {
        'form': form,
    }

    return render_to_response('forms/signup_form.html', data)


def edit_profile_form(request):

    if request.user.is_authenticated():

        profile = UserProfile.objects.get(user=request.user)

        data = {
            'user': request.user,
            'profile': profile,
        }

        form = ProfileForm(request.POST)

    return render_to_response('profile_form.html', data)