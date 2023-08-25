from django.shortcuts import render, get_object_or_404
from.models import Automobilio_modelis, Automobilis, Paslauga, Uzsakymas, Uzsakymoeilutes

def index(request):
    num_paslaugu_kiekis = Paslauga.objects.count()
    num_atliktu_uzsakymu_kiekis = Paslauga.objects.filter(status__exact='a').count()
    num_automobiliu_kiekis = Automobilis.objects.count()
    num_uzsakymas = Uzsakymas.objects.all().count()
    num_automobiliu_modeliai = Automobilio_modelis.objects.count()

    context_t = {
        'num_paslaugu_kiekis_t': num_paslaugu_kiekis,
        'num_atliktu_uzsakymu_kiekis_t': num_atliktu_uzsakymu_kiekis,
        'num_automobiliu_kiekis_t': num_automobiliu_kiekis,
        'num_uzsakymas_t': num_uzsakymas,
        'num_automobiliu_modeliai_t': num_automobiliu_modeliai
    }



    return render(request, 'index.html', context=context_t)


def automobiliai(request):
        automobiliai = Automobilis.objects.all()

        context_t = {
            'automobiliai_t': automobiliai
        }
        return render(request, 'automobilis.html', context=context_t)


def automobilis(request, automobilis):
    automobilis = get_object_or_404(Automobilis, pk=automobilis)

    return render(request, 'automobilis.html', context={'automobilis': automobilis})

