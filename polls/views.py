from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Image, State, User_states_image
from django.views import generic
from django.urls  import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
# Classify "image"
# Classify "vote"
# Back action
# Vote action


def register(request):
    image = Image.objects.get(pk = 1)
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            image = Image.objects.get(pk = 1)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return reverse('polls:vote', args = [image.pk])
    else:
        form = UserCreationForm()

    return render(request, 'polls/register.html', {'form': form})


def vote(request, image_id):
    image = get_object_or_404(Image, pk = image_id)
    states = get_object_or_404(State, pk = 1)

    try:
        selected_choice = states.objects.get(pk = request.POST['state'])
    except (KeyError):
        # Redisplay the question voting form.
        return reverse('polls:register')
    else:
        #Save out the User_states_image
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return reverse('polls:register')
