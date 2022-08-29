# Generated by Django 4.1 on 2022-08-28 10:01

import cpf_field.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArmarioAcervo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Armários',
                'ordering': ['codigo'],
            },
        ),
        migrations.CreateModel(
            name='FaceArmario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('armario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assentamento.armarioacervo', verbose_name='Armário')),
            ],
            options={
                'verbose_name_plural': 'Faces Armários',
                'ordering': ['codigo'],
            },
        ),
        migrations.CreateModel(
            name='Situacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Situações',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='PrateleiraFace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('face', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assentamento.facearmario', verbose_name='Face Armário')),
            ],
            options={
                'verbose_name_plural': 'Prateleiras faces',
                'ordering': ['codigo'],
            },
        ),
        migrations.CreateModel(
            name='AssentamentoFuncional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cpf', cpf_field.models.CPFField(blank=True, max_length=14, null=True, verbose_name='cpf')),
                ('matricula', models.CharField(max_length=10, verbose_name='Matricula SIAPE')),
                ('categoria_funcional', models.CharField(choices=[('Téc_Admin', 'Tecnico Administrativo'), ('Docente', 'Docente')], max_length=10, verbose_name='Categoria')),
                ('status_afd', models.BooleanField(default=False, verbose_name='Incluido no AFD')),
                ('obs', models.TextField(blank=True, null=True)),
                ('localizacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assentamento.prateleiraface', verbose_name='Local Assentamento')),
                ('situacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assentamento.situacao', verbose_name='Situação Servidor')),
            ],
            options={
                'verbose_name_plural': 'Assentamentos Funcionais',
                'ordering': ['nome'],
            },
        ),
    ]
