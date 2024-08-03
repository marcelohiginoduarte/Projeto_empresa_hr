from django.shortcuts import render, redirect
from .forms import CollaboratorForm


def criar_Collaborator(request):

    if request.method == 'POST':
        form = CollaboratorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ceatecolaborador')
    else:
        form = CollaboratorForm()

    return render(request, 'base.html', {'form': form})

def base(request):
    return render(request, 'base.html')



