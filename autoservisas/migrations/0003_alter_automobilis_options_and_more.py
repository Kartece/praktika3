# Generated by Django 4.2.4 on 2023-08-23 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autoservisas', '0002_automobilismodelis_paslauga_uzsakymas_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='automobilis',
            options={'verbose_name': 'Automobilis', 'verbose_name_plural': 'Automobiliai'},
        ),
        migrations.AlterModelOptions(
            name='automobilismodelis',
            options={'verbose_name': 'Automobilio modelis', 'verbose_name_plural': 'Automobilio modeliai'},
        ),
        migrations.AlterModelOptions(
            name='paslauga',
            options={'verbose_name': 'Paslauga', 'verbose_name_plural': 'Paslaugos'},
        ),
        migrations.AlterModelOptions(
            name='uzsakymas',
            options={'verbose_name': 'Uzsakymas', 'verbose_name_plural': 'Uzsakymai'},
        ),
        migrations.AlterModelOptions(
            name='uzsakymoeilutes',
            options={'verbose_name': 'Uzsakymo eilute', 'verbose_name_plural': 'Uzsakymo eilutes'},
        ),
    ]
