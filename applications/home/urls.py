#
from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path(
        'plantilla/', 
        views.TestPlantilla.as_view(),
        name='plantilla',
    ),  
    path(
        '', 
        views.HomePageView.as_view(),
        name='index',
    ),
    path(
        'index/', 
        views.HomePageView.as_view(),
        name='index',
    ),
    path(
        'subscriber/', 
        views.SuscriberCreateView.as_view(),
        name='subscriber',
    ),
    path(
        'contacto/', 
        views.ContactCreateView.as_view(),
        name='contacto',
    )
] 