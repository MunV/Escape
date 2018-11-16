from django.shortcuts import render

from .models import Salle


def index(request):
    salles = Salle.objects.all()
    context = {'liste_des_salles': salles}
    return render(request, 'home.html', context)
