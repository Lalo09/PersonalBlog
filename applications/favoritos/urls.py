#
from django.urls import path

from . import views

app_name = "favoritos_app"

urlpatterns = [
    path(
        'perfil/', 
        views.UserPageListView.as_view(),
        name='perfil',
    ),
    path(
        'add-entry/<pk>', 
        views.AddFavoriteView.as_view(),
        name='add-favoritos',
    ),
    path(
        'delete-favorites/<pk>', 
        views.RemoveFavoriteView.as_view(),
        name='delete-favoritos',
    )
]