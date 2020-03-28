from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

app_name = 'polls'
urlpatterns = [
    path('display_image/', views.display_image, name='display_image'),
    path('vote/', views.vote, name='vote'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('select_site/', views.select_site, name='select_site'),
    path('site_selection/', views.site_selection, name='site_selection')
    #path('', TemplateView.as_view(template_name="site_selection.html"), name='site_selection_page')
]

urlpatterns += staticfiles_urlpatterns() #bit confused here.
