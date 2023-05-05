
from django.contrib import admin
from django.urls import path
from appRafael import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('formtrofeus/', views.create_trofeus),
    path('formjogadores/', views.create_jogadores),
    path('trofeu/edit/<trofeu_id>', views.update_trofeu),
    path('trofeu/delete/<trofeu_id>', views.delete_trofeu),
    path('jogador/edit/<jogador_id>', views.update_jogador),
    path('jogador/delete/<jogador_id>', views.delete_jogador),
]
