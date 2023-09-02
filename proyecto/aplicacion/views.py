from django.shortcuts import render , redirect
from django.urls import reverse_lazy   
from django.http import HttpResponse 

from .models import Alquileres, Venta , Asesores, Avatar , Inversiones
from .forms import   RegistroUsuariosForm, UserEditForm, AvatarFormulario

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, update_last_login
from django.contrib.auth       import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.api import success


def home(request):
    return render (request, 'aplicacion/home.html') 


def alquiler(request):
    contexto= {'alquileres': Alquileres.objects.all() } 
    return render (request, 'aplicacion/alquiler.html', contexto) 


def venta(request):
    contexto= {'ventas': Venta.objects.all()}
    return render (request, 'aplicacion/venta.html',contexto)


def asesores(request):
    contexto = {'asesores': Asesores.objects.all()}
    return render (request,'aplicacion/asesores.html',contexto)


def inversiones(request):
    contexto = {'inversiones': Inversiones.objects.all()}
    return render (request, 'aplicacion/inversiones.html', contexto)

def about(request):
    return render(request, 'aplicacion/about.html', {})

#_________________________________________________________________________#
#                               CBS                                       #
#_________________________________________________________________________#

# Alquiler

class AlquilerCreate(LoginRequiredMixin, CreateView):
    model = Alquileres
    fields = ['tipo', 'ambientes', 'localidad', 'precio']
    success_url = reverse_lazy('alquiler')


class AlquilerUpdate(LoginRequiredMixin, UpdateView):
    model = Alquileres
    fields = ['tipo', 'ambientes', 'localidad', 'precio']
    success_url = reverse_lazy('alquiler')

class AlquilerDelete(LoginRequiredMixin, DeleteView):
    model = Alquileres
    success_url = reverse_lazy('alquiler')


#  Venta 

class VentaCreate(LoginRequiredMixin, CreateView):
    model = Venta
    fields = ['tipo', 'ambientes', 'localidad', 'precio']
    success_url = reverse_lazy('venta')


class VentaUpdate(LoginRequiredMixin, UpdateView):
    model = Venta
    fields = ['tipo', 'ambientes', 'localidad', 'precio']
    success_url = reverse_lazy('venta')

class VentaDelete(LoginRequiredMixin, DeleteView):
    model = Venta
    success_url = reverse_lazy('venta')

#  Inversiones 

class InversionCreate(LoginRequiredMixin, CreateView):
    model = Inversiones
    fields = ['etapa', 'ambientes', 'localidad', 'precio']
    success_url = reverse_lazy('inversiones')

class InversionUpdate(LoginRequiredMixin, UpdateView):
    model = Inversiones
    fields = ['etapa', 'ambientes', 'localidad', 'precio']
    success_url = reverse_lazy('inversiones')

class InversionDelete(LoginRequiredMixin, DeleteView):
    model = Inversiones
    success_url = reverse_lazy('inversiones')

#  Asesores 

class AsesorCreate(LoginRequiredMixin, CreateView):
    model = Asesores
    fields = ['nombre', 'apellido', 'telefono', 'email']
    success_url = reverse_lazy('asesores')

class AsesorUpdate(LoginRequiredMixin, UpdateView):
    model = Asesores
    fields = ['nombre', 'apellido', 'telefono', 'email']
    success_url = reverse_lazy('asesores')

class AsesorDelete(LoginRequiredMixin, DeleteView):
    model = Asesores
    success_url = reverse_lazy('asesores')


#___________________________________________________________________________________#
                            # Buscador #
#___________________________________________________________________________________#



def search(request):
    query = request.GET.get('q')  # Obtener el término de búsqueda de la URL
    
    if query == "":
        mensaje= 'No se ingreso nada para buscar'
        context= {'mensaje': mensaje}
        return render(request, 'aplicacion/search.html', context)
    elif query:
        alquileres_results = Alquileres.objects.filter(tipo__icontains=query)
        ventas_results = Venta.objects.filter(tipo__icontains=query)
        
        context = {
            'alquileres_results': alquileres_results,
            'ventas_results': ventas_results,
            'query': query,
        }
        return render(request, 'aplicacion/search.html', context)

#________________________________________________________________________________#
#                                   Login                                        # 
#________________________________________________________________________________#


def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)

                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar

                return render(request, "aplicacion/home.html", {'form': miForm})
            else:
                return render(request, "aplicacion/login.html", {'form': miForm})
        else:
            return render(request, "aplicacion/login.html", {'form': miForm})

    miForm =   AuthenticationForm()      

    return render(request, "aplicacion/login.html", {"form":miForm})    

  

 
def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
         
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "aplicacion/registro.html",{'mensaje': f' ¡El usuario: {usuario} se registro con exito!'})
    else:
        miForm =   RegistroUsuariosForm()      
    return render(request, "aplicacion/registro.html", {"form":miForm}) 

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email= form.cleaned_data.get('email')
            usuario.password1= form.cleaned_data.get('password1')
            usuario.password2= form.cleaned_data.get('password2')
            usuario.first_name= form.cleaned_data.get('first_name')
            usuario.last_name= form.cleaned_data.get('last_name')
            usuario.save ()
            return render (request, "aplicacion/home.html")
        else:
            return render (request, "aplicacion/editarPerfil.html", {"form": form, "usuario": usuario.username})
    else:
        form= UserEditForm(instance= usuario)
    return render (request, "aplicacion/editarPerfil.html", {"form":form , "usuario":usuario.username})
 
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"aplicacion/home.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form })
