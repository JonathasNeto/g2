from django import forms
from django.shortcuts import get_list_or_404

from .models import *

class FormSoli(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = ('origen','destino','data','quantidade')

class FormAtender(forms.Form):
    funcionario = get_list_or_404(Funcionario,eh_motorista=True)
    print (funcionario)
    class Meta:
        model = Atender
        fields = ('solicitacao','motorista','veiculo')
      


    
