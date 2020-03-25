from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Image, State, User_states_image
from django.views import generic
from django.urls  import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages


#To do :
# Create a view where the user can choose to register, or to login as a returning user.

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return HttpResponseRedirect(reverse('polls:display_image'))
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()

    return render(request = request,
                    template_name = "polls/login.html",
                    context={"form":form})

def register(request):

    if request.method == "POST":
        form = AuthenticationForm(request.POST)

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

    user_imgs = [uu.image for uu in User_states_image.objects.all() if uu.user == user] #retrieve all images the user has labelled
    not_categorized = [im for im in Image.objects.all() if im not in user_imgs] #which ones are not in the list

    image = get_object_or_404(Image, pk = not_categorized[0].pk) #can choose to randomize or not, for not take each one

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
