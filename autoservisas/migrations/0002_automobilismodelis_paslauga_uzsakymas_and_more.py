# Generated by Django 4.2.4 on 2023-08-22 12:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('autoservisas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Automobilismodelis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marke', models.CharField(blank=True, max_length=100, null=True, verbose_name='Marke')),
                ('modelis', models.CharField(max_length=100, verbose_name='Modelis')),
                ('metai', models.IntegerField(verbose_name='Metai')),
                ('variklis', models.CharField(max_length=100, verbose_name='Variklis')),
            ],
            options={
                'ordering': ['marke', 'modelis', 'variklis', 'metai'],
            },
        ),
        migrations.CreateModel(
            name='Paslauga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pavadinimas', models.TextField(max_length=1000, verbose_name='Pavadinimas')),
                ('kaina', models.FloatField(verbose_name='Kaina')),
                ('status', models.CharField(blank=True, choices=[('a', 'Patvirtinta'), ('p', 'Vykdoma'), ('g', 'Atlikta'), ('r', 'Atsaukta')], default='a', help_text='Statusas', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Uzsakymas',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('data', models.DateTimeField(blank=True, null=True, verbose_name='Bus grazinta')),
                ('suma', models.FloatField(verbose_name='Suma')),
            ],
        ),
        migrations.AlterModelOptions(
            name='automobilis',
            options={},
        ),
        migrations.RemoveField(
            model_name='automobilis',
            name='marke',
        ),
        migrations.RemoveField(
            model_name='automobilis',
            name='metai',
        ),
        migrations.RemoveField(
            model_name='automobilis',
            name='modelis',
        ),
        migrations.RemoveField(
            model_name='automobilis',
            name='variklis',
        ),
        migrations.AddField(
            model_name='automobilis',
            name='klientas',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Klientas'),
        ),
        migrations.AddField(
            model_name='automobilis',
            name='valstybiniai_nr',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Valstybiai nr'),
        ),
        migrations.AddField(
            model_name='automobilis',
            name='vin',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Vin'),
        ),
        migrations.CreateModel(
            name='Uzsakymoeilutes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kiekis', models.IntegerField(verbose_name='Kiekis')),
                ('kaina', models.FloatField(verbose_name='Kaina')),
                ('paslauga', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservisas.paslauga')),
                ('uzsakymas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservisas.uzsakymas')),
            ],
        ),
        migrations.AddField(
            model_name='uzsakymas',
            name='automobilis',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservisas.automobilis'),
        ),
        migrations.AddField(
            model_name='automobilis',
            name='automobilismodelis',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservisas.automobilismodelis'),
        ),
    ]