from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('<int:image_id>/vote/', views.vote, name='vote'),
    path('register/', views.register, name='register'),
]
