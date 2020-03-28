from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .models import Image, State, User_states_image
from django.views import generic
from django.urls  import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


#To do :
# Create a view where the user can choose to register, or to login as a returning user.

def logout_request(request):
    logout(request)
    messages.info(request, 'Logged out successfully!')
    return redirect('polls:login')


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
                return render(request,'polls/site_selection.html')
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
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            image = Image.objects.get(pk = 3)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return render(request,'polls/site_selection.html')
        else:
            messages.error(request, "Try registering again")
    else:
        form = UserCreationForm()

    return render(request, 'polls/register.html', {'form': form})

def display_image(request):
    user = request.user
    site = request.session.get('site')

    site_text_dict = {'nbn':'c5', 'duck':'rect.jpg'}
    site_text = site_text_dict[site]

    user_imgs = [uu.image for uu in User_states_image.objects.all() if uu.user == user] #retrieve all images the user has labelled
    not_categorized = [im for im in Image.objects.all() if im not in user_imgs] #which ones are not in the list
    site_imgs = [im for im in not_categorized if site_text in im.filename]

    image = get_object_or_404(Image, pk = site_imgs[0].pk) #can choose to randomize or not, for not take each one

    return render(request, 'polls/display_image.html', {'image': image, 'states':State.objects.all(), 'site':site})


def vote(request):
    image_id = request.POST['image_pk']
    image = get_object_or_404(Image, pk = image_id)
    user = request.user

    state = request.POST.get('state')

    selected_choice = State.objects.get(pk = state)

    if len(User_states_image.objects.filter(image=image, user=user)) >= 1:
        uu = User_states_image.objects.get(image=image, user=user)
        uu.delete()

    User_states_image.objects.create(state = selected_choice, image = image, user = user)

    return HttpResponseRedirect(reverse('polls:display_image'))


def select_site(request):
    site = request.POST['site']
    request.session['site'] = site
    return redirect('polls:display_image')

def site_selection(request):
    #can i do this without having a view??
    return render(request, 'polls/site_selection.html')