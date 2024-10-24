# Generated by Django 5.1.2 on 2024-10-23 20:46

import Core.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to=Core.models.Estacao.gerar_rota_icon)),
                ('descricao_estacao', models.TextField(max_length=2000)),
                ('texto_funcionamento', models.TextField(max_length=1000)),
                ('servico1', models.CharField(max_length=100)),
                ('servico2', models.CharField(max_length=100)),
                ('servico3', models.CharField(max_length=100)),
                ('responsabilidade', models.TextField(max_length=1000)),
                ('beneficio1', models.CharField(max_length=1000)),
                ('beneficio2', models.CharField(max_length=1000)),
                ('beneficio3', models.CharField(max_length=1000)),
                ('ideal_para1', models.CharField(max_length=1000)),
                ('ideal_para2', models.CharField(max_length=1000)),
                ('ideal_para3', models.CharField(max_length=1000)),
                ('competencia', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Paleta_Core',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cor_principal', models.CharField(max_length=7)),
                ('cor_detalhes', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Imagens_equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to=Core.models.Imagens_equipe.gerar_rota)),
                ('alt', models.CharField(max_length=100)),
                ('estacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.estacao')),
            ],
        ),
        migrations.CreateModel(
            name='Imagens_beneficios_core',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt', models.CharField(max_length=100)),
                ('imagem', models.ImageField(upload_to=Core.models.Imagens_beneficios_core.gerar_rota)),
                ('cor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.paleta_core')),
            ],
        ),
        migrations.CreateModel(
            name='Ideal_para',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to=Core.models.Ideal_para.gerar_rota)),
                ('cor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.paleta_core')),
            ],
        ),
        migrations.AddField(
            model_name='estacao',
            name='cor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.paleta_core'),
        ),
        migrations.CreateModel(
            name='Beneficio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to=Core.models.Beneficio.gerar_rota)),
                ('cor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.paleta_core')),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt', models.CharField(max_length=100)),
                ('imagem', models.ImageField(upload_to=Core.models.Servico.gerar_rota)),
                ('cor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.paleta_core')),
            ],
        ),
    ]
