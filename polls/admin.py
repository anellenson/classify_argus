from django.contrib import admin
from .models import Image, State, User_states_image

admin.site.register(Image)
admin.site.register(State)
admin.site.register(User_states_image)

# Register your models here.
