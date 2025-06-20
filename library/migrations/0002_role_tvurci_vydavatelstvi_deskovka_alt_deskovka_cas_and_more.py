# Generated by Django 5.2.1 on 2025-05-28 10:36

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(help_text='Zadejte název role', max_length=80, verbose_name='Název role')),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Role',
            },
        ),
        migrations.CreateModel(
            name='Tvurci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jmeno', models.CharField(help_text='Zadejte jméno tvůrce', max_length=80, verbose_name='Jméno tvůrce')),
                ('Prijmeni', models.CharField(help_text='Zadejte příjmení tvůrce', max_length=80, verbose_name='Příjmení tvůrce')),
                ('zivotopis', models.TextField(help_text='Zadejte životopis tvůrce', verbose_name='Životopis')),
            ],
            options={
                'verbose_name': 'Tvůrce',
                'verbose_name_plural': 'Tvůrci',
            },
        ),
        migrations.CreateModel(
            name='Vydavatelstvi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jmeno', models.CharField(help_text='Zadejte jméno vydavatelství', max_length=80, verbose_name='Jméno vydavatelství')),
            ],
            options={
                'verbose_name': 'Vydavatelství',
                'verbose_name_plural': 'Vydavatelství',
            },
        ),
        migrations.AddField(
            model_name='deskovka',
            name='alt',
            field=models.CharField(default='', help_text='Zadejte alternativní jméno deskové hry', max_length=80, verbose_name='Alternativní jméno deskové hry'),
        ),
        migrations.AddField(
            model_name='deskovka',
            name='cas',
            field=models.IntegerField(default=0, help_text='Zadejte délku hry v minutách', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)], verbose_name='Délka hry'),
        ),
        migrations.AddField(
            model_name='deskovka',
            name='komplexita',
            field=models.PositiveIntegerField(choices=[(0, ''), (1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')], default=3, verbose_name='Komplexita hry'),
        ),
        migrations.AddField(
            model_name='deskovka',
            name='minvek',
            field=models.IntegerField(default=0, help_text='Zadejte minimální věk', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)], verbose_name='Minimální věk'),
        ),
        migrations.AddField(
            model_name='deskovka',
            name='nazev',
            field=models.CharField(default='', error_messages={'blank': 'Jméno deskové hry musí být vyplněno'}, help_text='Zadejte jméno deskové hry', max_length=80, verbose_name='Jméno deskové hry'),
        ),
        migrations.AddField(
            model_name='deskovka',
            name='pocet_hrac',
            field=models.IntegerField(default=1, help_text='Zadejte počet hráčů', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)], verbose_name='Počet hráčů'),
        ),
        migrations.AddField(
            model_name='deskovka',
            name='popis',
            field=models.TextField(default='', help_text='Zadejte popis deskové hry', verbose_name='Popis'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='DeskovkaZanr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deskovka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deskovka_zanr', to='library.deskovka')),
                ('zanr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zanr_deskovka', to='library.zanr')),
            ],
            options={
                'verbose_name': 'Žánr deskovky',
                'verbose_name_plural': 'Žánry deskovek',
            },
        ),
        migrations.CreateModel(
            name='Hodnoceni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hodnoceni', models.IntegerField(help_text='Zadejte hodnocení', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Hodnocení')),
                ('datum', models.DateField(auto_now_add=True, verbose_name='Datum hodnocení')),
                ('recenze', models.TextField(help_text='Zadejte recenzi', verbose_name='Recenze')),
                ('Hra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hodnoceni_set', to='library.deskovka')),
                ('uzivatel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hodnoceni', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Hodnocení',
                'verbose_name_plural': 'Hodnocení',
            },
        ),
        migrations.CreateModel(
            name='Rozsireni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(help_text='Zadejte název rozšíření', max_length=80, verbose_name='Název rozšíření')),
                ('vydani', models.DateField(blank=True, null=True, verbose_name='Datum vydaní')),
                ('popis', models.TextField(help_text='Zadejte popis rozšíření', verbose_name='Popis')),
                ('fotografie', models.ImageField(blank=True, null=True, upload_to='rozsireni', verbose_name='Fotografie')),
                ('deskovka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rozsirena_deskovka', to='library.deskovka')),
            ],
            options={
                'verbose_name': 'Rozšíření',
                'verbose_name_plural': 'Rozšíření',
            },
        ),
        migrations.CreateModel(
            name='TvurceRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_tvurce', to='library.role')),
                ('tvurce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tvurce_role', to='library.tvurci')),
            ],
            options={
                'verbose_name': 'Role tvůrce',
                'verbose_name_plural': 'Role tvůrců',
            },
        ),
        migrations.CreateModel(
            name='DeskovkaTvurce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deskovka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deskovka_tvurce', to='library.deskovka')),
                ('tvurce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tvurce_deskovka', to='library.tvurci')),
            ],
            options={
                'verbose_name': 'Tvůrce deskovky',
                'verbose_name_plural': 'Tvůrci deskovek',
            },
        ),
        migrations.CreateModel(
            name='DeskovkaVydavatelstvi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deskovka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deskovka_vydavatelstvi', to='library.deskovka')),
                ('vydavatelstvi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vydavatelstvi_deskovka', to='library.vydavatelstvi')),
            ],
            options={
                'verbose_name': 'Vydavatelství deskovky',
                'verbose_name_plural': 'Vydavatelství deskovek',
            },
        ),
        migrations.DeleteModel(
            name='Prehled',
        ),
    ]
