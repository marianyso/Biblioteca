from django.contrib import admin
from django.urls import path
from app.views import (
    IndexView, LivrosView, CidadesView, 
    AutoresView, EditorasView, LeitoresView, 
    GenerosView, DeleteLivroView  # Importando a DeleteLivroView que não estava na importação
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('livros/', LivrosView.as_view(), name='livros'),
    # path('reserva/', EmprestimoView.as_view(), name='reserva'),  # Comentado se você quiser ativar depois
    path('cidade/', CidadesView.as_view(), name='cidade'),
    path('autor/', AutoresView.as_view(), name='autor'),
    path('editor/', EditorasView.as_view(), name='editora'),
    path('leitor/', LeitoresView.as_view(), name='leitor'),
    path('genero/', GenerosView.as_view(), name='genero'),
    path('delete/<int:id>/', DeleteLivroView.as_view(), name='delete'), 
]
