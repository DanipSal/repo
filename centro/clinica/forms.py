from django import forms



class Pacientes_formulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    DNI = forms.IntegerField()
    nacimiento = forms.DateField()

class Medico_formulario(forms.Form):
    Medico = forms.CharField(max_length=40)
    especialidad = forms.CharField(max_length=40)

class Turnos_formulario(forms.Form):
    fechaturno = forms.DateField()
    especialidad = forms.CharField(max_length=40)