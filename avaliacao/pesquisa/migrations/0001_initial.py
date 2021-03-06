# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 14:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='nome')),
                ('dataInicio', models.DateTimeField(verbose_name='data_inicio_curso')),
                ('dataFim', models.DateTimeField(verbose_name='data_fim_curso')),
                ('professor', models.CharField(max_length=100, verbose_name='professor')),
                ('codigo', models.CharField(max_length=10, verbose_name='chave_acesso')),
            ],
        ),
        migrations.CreateModel(
            name='pesquisa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questao1', models.CharField(choices=[('0', 'Discordo Totalmente'), ('1', 'Discordo'), ('2', 'Nem concordo, nem discordo'), ('3', 'Concordo'), ('4', 'Concordo Totalmente')], max_length=1)),
                ('questao2', models.CharField(choices=[('0', 'Discordo Totalmente'), ('1', 'Discordo'), ('2', 'Nem concordo, nem discordo'), ('3', 'Concordo'), ('4', 'Concordo Totalmente')], max_length=1)),
                ('questao3', models.CharField(choices=[('0', 'Discordo Totalmente'), ('1', 'Discordo'), ('2', 'Nem concordo, nem discordo'), ('3', 'Concordo'), ('4', 'Concordo Totalmente')], max_length=1)),
                ('questao4', models.CharField(choices=[('0', 'Discordo Totalmente'), ('1', 'Discordo'), ('2', 'Nem concordo, nem discordo'), ('3', 'Concordo'), ('4', 'Concordo Totalmente')], max_length=1)),
                ('questao5', models.CharField(choices=[('0', 'Discordo Totalmente'), ('1', 'Discordo'), ('2', 'Nem concordo, nem discordo'), ('3', 'Concordo'), ('4', 'Concordo Totalmente')], max_length=1)),
                ('questao6', models.CharField(choices=[('0', 'Discordo Totalmente'), ('1', 'Discordo'), ('2', 'Nem concordo, nem discordo'), ('3', 'Concordo'), ('4', 'Concordo Totalmente')], max_length=1)),
                ('questao7', models.CharField(choices=[('0', 'Discordo Totalmente'), ('1', 'Discordo'), ('2', 'Nem concordo, nem discordo'), ('3', 'Concordo'), ('4', 'Concordo Totalmente')], max_length=1)),
                ('questao8', models.CharField(choices=[('0', 'Discordo Totalmente'), ('1', 'Discordo'), ('2', 'Nem concordo, nem discordo'), ('3', 'Concordo'), ('4', 'Concordo Totalmente')], max_length=1)),
                ('questao9', models.CharField(choices=[('1', 'Sim'), ('0', 'Não')], max_length=1)),
                ('comentario', models.CharField(max_length=200)),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pesquisa.curso')),
            ],
        ),
    ]
