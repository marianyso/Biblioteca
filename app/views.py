from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages  # Importando messages para feedbacks de sucesso ou erro
from .models import Livro, Cidade, Autor, Editora, Leitor, Genero

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class LivrosView(View):
    def get(self, request, *args, **kwargs):
        livros = Livro.objects.all()
        return render(request, 'livros.html', {'livros': livros})

# Descomentando o código de EmprestimoView se necessário, caso contrário, ele pode permanecer comentado
# class EmprestimoView(View):
#     def get(self, request, *args, **kwargs):
#         reservas = Emprestimo.objects.all()
#         return render(request, 'reserva.html', {'reservas': reservas})

class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})

class AutoresView(View):
    def get(self, request, *args, **kwargs):
        autores = Autor.objects.all()
        return render(request, 'autor.html', {'autores': autores})

class EditorasView(View):
    def get(self, request, *args, **kwargs):
        editoras = Editora.objects.all()
        return render(request, 'editora.html', {'editoras': editoras})

class LeitoresView(View):
    def get(self, request, *args, **kwargs):
        leitores = Leitor.objects.all()
        return render(request, 'leitor.html', {'leitores': leitores})

class GenerosView(View):
    def get(self, request, *args, **kwargs):
        generos = Genero.objects.all()
        return render(request, 'genero.html', {'generos': generos})

class DeleteLivroView(View):
    def get(self, request, id, *args, **kwargs):
        livro = get_object_or_404(Livro, id=id)  # Usando get_object_or_404 para evitar erro se o livro não for encontrado
        livro.delete()
        messages.success(request, 'Livro excluído com sucesso!')  # Exibindo mensagem de sucesso
        return redirect('livros')  # Redirecionando de volta para a lista de livros
