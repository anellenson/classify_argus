from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'polls'
urlpatterns = [
    path('display_image/', views.display_image, name='display_image'),
    path('vote/', views.vote, name='vote'),
    path('register/', views.register, name='register'),
]

urlpatterns += staticfiles_urlpatterns() #bit confused here.
