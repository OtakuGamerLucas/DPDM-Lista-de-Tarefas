from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TarefaForm, self).__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Tarefa
        fields = [
            'tarefa'
        ]