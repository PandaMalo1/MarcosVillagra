from django.shortcuts import render
from .forms import LibroBusquedaForm
from .models import Libro

def buscar_libros(request):
    form = LibroBusquedaForm(request.GET or None)
    resultado = []
    if form.is_valid():
        titulo = form.cleaned_data.get('titulo')
        autor = form.cleaned_data.get('autor')
        resultado = Libro.objects.all()
        if titulo:
            resultado = resultado.filter(titulo_icontains=titulo)
        if autor: 
            resultado = resultado.filter(autor_nombre_icontains=autor)
        return render(request, 'buscar_libros.html', {'form': form, 'resultado': resultado})
    