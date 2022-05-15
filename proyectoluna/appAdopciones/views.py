from django.shortcuts import render
from appAdopciones.models import Pet

# Create your views here.
def Pets(request):
    pets=Pet.objects.all()
    return render(request, "pets/pets.html", {"pets": pets})