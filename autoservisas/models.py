from django.db import models


import uuid

# Create your models here.

class Automobilio_modelis(models.Model):
    metai = models.IntegerField('Metai')
    marke = models.CharField('Markė', max_length=200)
    modelis = models.CharField('Modelis', max_length=200)
    variklis = models.CharField('Variklis', max_length=200)

    def __str__(self):
        return f"{self.metai}, {self.marke} {self.modelis}, {self.variklis}"

    class Meta:
        verbose_name = 'Automobilio modelis'
        verbose_name_plural = 'Automobilio modeliai'

    def __str__(self):
        return f"{self.marke} {self.modelis} {self.metai} {self.variklis}"


class Automobilis(models.Model):
    valstybiniai_nr = models.CharField('Valstybiai nr', max_length=6, null=True, blank=True)
    vin = models.CharField('Vin', max_length=10, null=True, blank=True)
    klientas = models.CharField('Klientas', max_length=100, null=True, blank=True)
    automobilio_mod_id = models.ForeignKey('Automobilio_modelis', on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f"{self.automobilio_mod_id.marke} {self.automobilio_mod_id.modelis} {self.valstybiniai_nr} {self.klientas}"

    class Meta:
        verbose_name = 'Automobilis'
        verbose_name_plural = 'Automobiliai'

class Uzsakymas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    data = models.DateTimeField('Bus grazinta', null=True, blank=True)
    suma = models.FloatField("Suma")
    automobilis_id = models.ForeignKey('Automobilis', on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f"{self.automobilis_id.klientas} {self.automobilis_id.valstybiniai_nr}, {self.automobilis_id}, {self.suma}"

    class Meta:
        verbose_name = 'Uzsakymas'
        verbose_name_plural = 'Uzsakymai'

class Paslauga(models.Model):
    pavadinimas = models.CharField("Pavadinimas", max_length=1000)
    kaina = models.FloatField("Kaina")

    LOAN_STATUS = (
        ('a', 'Patvirtinta'),
        ('p', 'Vykdoma'),
        ('g', 'Atlikta'),
        ('r', 'Atsaukta')
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Statusas'
    )


    def __str__(self):
        return f"{self.pavadinimas} {self.kaina}"

    class Meta:
        verbose_name = 'Paslauga'
        verbose_name_plural = 'Paslaugos'

class Uzsakymoeilutes(models.Model):
    kiekis = models.IntegerField("Kiekis")
    kaina = models.FloatField("Kaina")
    uzsakymas_id = models.ForeignKey("Uzsakymas", on_delete=models.SET_NULL, null=True)
    paslauga_id = models.ForeignKey("Paslauga", on_delete=models.SET_NULL, null=True)



    def __str__(self):
        return f"{self.paslauga.id} {self.kiekis} {self.kaina} "

    class Meta:
        verbose_name = 'Uzsakymo eilute'
        verbose_name_plural = 'Uzsakymo eilutes'






