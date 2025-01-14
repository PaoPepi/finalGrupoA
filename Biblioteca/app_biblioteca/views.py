from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from app_biblioteca.models import Libro
from app_biblioteca.forms import LibroFormulario, SocioFormulario, CursoFormulario
from app_biblioteca.models import Cursos, Socio
from django.db.models.functions import Lower, Replace

def inicio(request):

    return render(request, "inicio.html")


def libros(request):

      if request.method == 'POST':

            miFormulario = LibroFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  libro = Libro (nombre=informacion['nombre'], autor=informacion['autor'],
                  publicacion=informacion["publicacion"], genero=informacion["genero"],
                  editorial=informacion["editorial"] )

                  libro.save()

                  return render(request, "inicio.html") 

      else: 

            miFormulario= LibroFormulario()

      return render(request, "libros.html", {"miFormulario":miFormulario})

	


def cursos(request):

      if request.method == 'POST':

            miFormularioCurso = CursoFormulario(request.POST)

            print(miFormularioCurso)

            if miFormularioCurso.is_valid:

                  informacion = miFormularioCurso.cleaned_data

                  curso = Cursos (nombre=informacion["nombre"],
                  codigocurso=informacion["codigocurso"], 
                  docente=informacion["docente"], diahorario=informacion["diahorario"] )

                  curso.save()

                  return render(request, "inicio.html") 

      else: 

            miFormularioCurso= CursoFormulario()

      return render(request, "cursos.html", {"miFormularioCurso":miFormularioCurso}) 



def socios(request):

      if request.method == 'POST':

            miFormulario = SocioFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  socio = Socio(nombre=informacion["nombre"], documento=informacion["documento"],
                  mail=informacion["mail"], telefono=informacion["telefono"] )

                  socio.save()

                  return render(request, "inicio.html") 

      else: 

            miFormulario= SocioFormulario()

      return render(request, "socios.html", {"miFormulario":miFormulario})



def catalogo(request):

    catalogo = Libro.objects.all()

    return render (request, 'catalogo.html', {'catalogo':catalogo} )


def listadocursos (request):

    listacurso = Cursos.objects.all()

    return render (request, 'listadocursos.html', {'listacurso':listacurso} )  


def buscarLibro (request):

      return render(request, 'buscarlibro.html')

def buscar(request):
      if request.method == "GET":

            libro = request.GET["libro"].lower()
            libros= Libro.objects.filter(nombre__icontains=libro)

            return render(request, "resultado.html",{"libro": libro, "libros": libros})
     

      else: 
           respuesta=  "No se encuentra el libro"

      return HttpResponse(respuesta)

def creatucuenta (request):

      return render(request, 'creatucuenta.html')

def accesoasocios (request):

      return render (request, 'accesoasocios.html')

