from django import forms

class PeliculaFormulario(forms.Form):
    nombreOriginal = forms.CharField(max_length=100)
    nombreTraduccion = forms.CharField(max_length=100)
    fechaDeEstreno = forms.DateField()
    genero = forms.CharField(max_length=100)
    director = forms.CharField(max_length=100)
    guionista = forms.CharField(max_length=100)
    sinopsis = forms.CharField(max_length=500)
    
class SerieFormulario(forms.Form):
    nombreOriginal = forms.CharField(max_length=100)
    nombreTraduccion = forms.CharField(max_length=100)
    fechaDeEstreno = forms.DateField()
    genero = forms.CharField(max_length=100)
    guionista = forms.CharField(max_length=100)
    temporadasEmitidas = forms.IntegerField()
    sinopsis = forms.CharField(max_length=500)
    
class VideoFormulario(forms.Form):
    nombreOriginal = forms.CharField(max_length=100)
    nombreTraduccion = forms.CharField(max_length=100)
    fechaDeEstreno = forms.DateField()
    genero = forms.CharField(max_length=100)
    creador = forms.CharField(max_length=100)
    plataforma = forms.CharField(max_length=100)
    sinopsis = forms.CharField(max_length=500)