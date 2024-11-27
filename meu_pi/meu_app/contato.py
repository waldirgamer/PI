from django.shortcuts import render, get_object_or_404, redirect
from .models import Contato
from .forms import ContatoForm

# CREATE
def criar_contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_contatos')
    else:
        form = ContatoForm()
    return render(request, 'criar_contato.html', {'form': form})

# READ
def listar_contatos(request):
    contatos = Contato.objects.all()
    return render(request, 'listar_contatos.html', {'contatos': contatos})

# UPDATE
def atualizar_contato(request, id):
    contato = get_object_or_404(Contato, id=id)
    if request.method == 'POST':
        form = ContatoForm(request.POST, instance=contato)
        if form.is_valid():
            form.save()
            return redirect('listar_contatos')
    else:
        form = ContatoForm(instance=contato)
    return render(request, 'atualizar_contato.html', {'form': form})

# DELETE
def excluir_contato(request, id):
    contato = get_object_or_404(Contato, id=id)
    if request.method == 'POST':
        contato.delete()
        return redirect('listar_contatos')
    return render(request, 'excluir_contato.html', {'contato': contato})
