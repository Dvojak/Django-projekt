# Generated by Django 5.2.1 on 2025-06-09 21:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_alter_tvurci_zivotopis'),
    ]

    operations = [
        migrations.AddField(
            model_name='deskovka',
            name='zanr',
            field=models.ForeignKey(blank=True, help_text='Vyberte žánr deskové hry', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deskovka_zanr', to='library.zanr', verbose_name='Žánr deskové hry'),
        ),
    ]
