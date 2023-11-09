from django.shortcuts import render
from Actor.forms import ActorForm
from Actor.models import Actor


def agregarActor(request):
    form = ActorForm()
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            form.save()
        #return index(request)
    data = {'form': form}
    return render(request,'Actor/agregarActor.html', data)

def listadoActor(request):
    actores = Actor.objects.all()
    data = {'actores': actores}
    return render (request, 'Actor/listaActor.html', data)

def pantallaInicio(request):
    return render(request,'Actor/index.html')

def eliminarActor(request, id):
    actores = Actor.objects.get(id=id)
    actores.delete()
    return render(request,'Actor')

def actualizarActor(request, id):
    actores = Actor.objects.get(id = id)
    form = ActorForm(instance=actores) 
    if request.method == 'POST':
        form = ActorForm(request.POST, instance=actores) 
        if form.is_valid():
            form.save()
        return pantallaInicio(request)
    data = {'form' : form}
    return render(request, 'Actor/agregarActor.html', data)
