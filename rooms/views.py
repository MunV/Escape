from django.http import HttpResponse


def index(request):
    return HttpResponse("Acceuil")

def detail(request, salle_id):
    return HttpResponse("Salle numero %s." % salle_id)

def reserve(request, salle_id):
    return HttpResponse("Vous reservez la salle %s." % salle_id)
