from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, View, DeleteView
from applications.entrada.models import Entry
from .models import Favorites

class UserPageListView(LoginRequiredMixin,ListView):
    template_name = "favoritos/perfil.html"
    context_object_name = 'entradas_user'
    login_url = reverse_lazy('users_app:user-login')

    def get_queryset(self):
        return Favorites.objects.entradas_user(self.request.user)

class AddFavoriteView(LoginRequiredMixin,View):
    login_url = reverse_lazy('users_app:user-login')

    def post(self,request,*args,**kwargs):

        #Recuperar usuario y id de entrada actual
        usuario = self.request.user
        entrada = Entry.objects.get(id=self.kwargs['pk'])

        #Registrar a favoritos
        Favorites.objects.create(
            user=usuario,
            entry = entrada
        )

        return HttpResponseRedirect(
            reverse(
                'favoritos_app:perfil'
            )
        )

class RemoveFavoriteView(DeleteView):
    model = Favorites
    success_url="/perfil"