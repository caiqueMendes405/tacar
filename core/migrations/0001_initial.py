# Generated by Django 4.1.7 on 2023-03-16 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(blank=True, max_length=100, null=True, verbose_name='Endereço')),
                ('complemento', models.CharField(blank=True, max_length=100, null=True, verbose_name='Complemento')),
                ('bairro', models.CharField(blank=True, max_length=100, null=True, verbose_name='Bairro')),
                ('cidade', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('fone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='foto_cliente', verbose_name='Foto')),
            ],
        ),
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Fabricante')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Site')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo_fabricante', verbose_name='url')),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=20, verbose_name='placa')),
                ('modelo', models.CharField(blank=True, max_length=30, null=True, verbose_name='Modelo')),
                ('cor', models.CharField(blank=True, max_length=30, null=True, verbose_name='Cor')),
                ('ano', models.IntegerField(blank=True, default=2023, null=True, verbose_name='Ano')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='foto_carro', verbose_name='')),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.cliente', verbose_name='Cliente')),
                ('fabricante_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.fabricante', verbose_name='Fabricante')),
            ],
        ),
    ]
