from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CommandeForm
from .forms import Commande
from django.contrib.auth.decorators import login_required



@login_required(login_url='acces')
def list_commande(request):
    return render(request, 'commande/list_commande.html')
@login_required(login_url='acces')
def ajouter_commande(request):
    form = CommandeForm()
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'commande/ajouter_commande.html', context)
@login_required(login_url='acces')
def modifier_commande(request,pk):
    commande = Commande.objects.get(id=pk)
    form = CommandeForm(instance=commande)

    if request.method == 'POST':
        form = CommandeForm(request.POST,instance=commande)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'commande/ajouter_commande.html', context)
@login_required(login_url='acces')
def supprimer_commande(request,pk):
    commande = Commande.objects.get(id=pk)
    if request.method == 'POST':
        commande.delete()
        return redirect('/')
    context={'item':commande}
    return render(request, 'commande/supprimer_commande.html', context)