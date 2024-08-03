from django import forms
from GestaoHR.models import collaborator

class CollaboratorForm(forms.ModelForm):
    class Meta:
        model = collaborator
        fields = ['Nome', 'CPF', 'Data_contratacao']
        