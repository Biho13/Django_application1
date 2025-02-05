# Generated by Django 5.1.2 on 2024-10-31 09:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('commande', '0001_initial'),
        ('produit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.client'),
        ),
        migrations.AlterField(
            model_name='commande',
            name='produit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='produit.produit'),
        ),
    ]
