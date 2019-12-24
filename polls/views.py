from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
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

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            image = Image.objects.get(pk = 3)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return HttpResponseRedirect(reverse('polls:display_image'))
    else:
        form = UserCreationForm()

    return render(request, 'polls/register.html', {'form': form})

def display_image(request):
    user = request.user

    user_objects = [uu for uu in User_states_image.objects.all() if uu == user] #retrieve all user objects
    user_imgs = [uu.image for uu in user_objects]
    not_categorized = [im for im in Image.objects.all() if im not in user_imgs] #which ones are not in the list
    image = get_object_or_404(Image, pk = not_categorized[0].pk) #can choose to randomie or not

    return render(request, 'polls/display_image.html', {'image': image, 'states':State.objects.all()})



def vote(request):
    image_id = request.POST['image_pk']
    image = get_object_or_404(Image, pk = image_id)
    user = request.user

    states = request.POST.getlist('state')
    for state in states:
        selected_choice = State.objects.get(pk = state)
        User_states_image.objects.create(state = selected_choice, image = image, user = user)

    return HttpResponseRedirect(reverse('polls:display_image'))
