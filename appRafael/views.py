from django.shortcuts import render,redirect
from .models import Trofeus,Jogadores

def home(request):
    trofeus = Trofeus.objects.all()
    jogadores = Jogadores.objects.all()
    context = {"trofeus": trofeus, "jogadores":jogadores}
    return render(request, "home.html", context=context)


def create_trofeus(request):
    if request.method == "POST":
       Trofeus.objects.create(nome=request.POST["nome"],
                               data=request.POST["data"],
                               descricao=request.POST["descricao"])
       return redirect("home")

    return render(request, "trofeus_form.html")

def create_jogadores(request):
    if request.method == "POST":
        if "aprovação" not in request.POST:
            aprovação = False
        else:
            aprovação = True
        Jogadores.objects.create(nome=request.POST["nome"],
                             posicao=request.POST["posicao"],
                             numero_camisa=request.POST["numero_camisa"],
                             caracteristicas=request.POST["caracteristicas"],
                                 aprovação=aprovação)
        return redirect("home")

    return render(request, "jogadores_form.html")

def update_trofeu(request, trofeu_id):
    trofeu = Trofeus.objects.get(id=trofeu_id)

    trofeu.data = trofeu.data.strftime('%Y-%m-%d')
  
    if request.method == "POST":
        trofeu.nome = request.POST["nome"]
        trofeu.data = request.POST["data"]
        trofeu.descricao = request.POST["descricao"]
        trofeu.save()
        return redirect("home")

    return render(request, "trofeus_form.html", context={"trofeu": trofeu})


def delete_trofeu(request, trofeu_id):
    trofeu = Trofeus.objects.get(id=trofeu_id)
    if request.method == "POST":
        if "confirm" in request.POST:
            trofeu.delete()
            return redirect("home")

    return render(request, "delete_trofeu.html", context={"trofeu": trofeu})

def update_jogador(request, jogador_id):
    jogador = Jogadores.objects.get(id=jogador_id)
  
    if request.method == "POST":
        jogador.nome = request.POST["nome"]
        jogador.posicao = request.POST["posicao"]
        jogador.numero_camisa = request.POST["numero_camisa"]
        jogador.caracteristicas = request.POST["caracteristicas"]
        if "aprovação" not in request.POST:
            jogador.aprovação = False
        else:
            jogador.aprovação = True
        jogador.save()
        return redirect("home")

    return render(request, "jogadores_form.html", context={"jogador": jogador})

def delete_jogador(request, jogador_id):
   jogador = Jogadores.objects.get(id=jogador_id)
   if request.method == "POST":
        if "confirm" in request.POST:
            jogador.delete()
            return redirect("home")

   return render(request, "delete_jogadores.html", context={"jogador": jogador})