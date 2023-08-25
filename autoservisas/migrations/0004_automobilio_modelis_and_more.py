# Generated by Django 4.2.4 on 2023-08-25 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autoservisas', '0003_alter_automobilis_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Automobilio_modelis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metai', models.IntegerField(verbose_name='Metai')),
                ('marke', models.CharField(max_length=200, verbose_name='Markė')),
                ('modelis', models.CharField(max_length=200, verbose_name='Modelis')),
                ('variklis', models.CharField(max_length=200, verbose_name='Variklis')),
            ],
            options={
                'verbose_name': 'Automobilio modelis',
                'verbose_name_plural': 'Automobilio modeliai',
            },
        ),
        migrations.RenameField(
            model_name='uzsakymas',
            old_name='automobilis',
            new_name='automobilis_id',
        ),
        migrations.RenameField(
            model_name='uzsakymoeilutes',
            old_name='paslauga',
            new_name='paslauga_id',
        ),
        migrations.RenameField(
            model_name='uzsakymoeilutes',
            old_name='uzsakymas',
            new_name='uzsakymas_id',
        ),
        migrations.RemoveField(
            model_name='automobilis',
            name='automobilismodelis',
        ),
        migrations.AlterField(
            model_name='paslauga',
            name='pavadinimas',
            field=models.CharField(max_length=1000, verbose_name='Pavadinimas'),
        ),
        migrations.DeleteModel(
            name='Automobilismodelis',
        ),
        migrations.AddField(
            model_name='automobilis',
            name='automobilio_mod_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservisas.automobilio_modelis'),
        ),
    ]
