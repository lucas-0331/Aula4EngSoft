# Generated by Django 4.2.5 on 2023-09-26 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('site', models.CharField(max_length=255)),
                ('insta', models.CharField(max_length=255)),
                ('face', models.CharField(max_length=255)),
                ('twitter', models.CharField(max_length=255)),
                ('nacionalidade', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Continente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Diretor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('site', models.CharField(max_length=255)),
                ('insta', models.CharField(max_length=255)),
                ('face', models.CharField(max_length=255)),
                ('twitter', models.CharField(max_length=255)),
                ('nacionalidade', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Epsodio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('duracao', models.DecimalField(decimal_places=2, max_digits=6)),
                ('data_disponivel', models.DateField(verbose_name='data_disponivel')),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('continente', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('duracao', models.DecimalField(decimal_places=2, max_digits=7)),
                ('sinopse', models.CharField(max_length=255)),
                ('site', models.CharField(max_length=255)),
                ('data_lancamento', models.DateField(verbose_name='data_lancamento')),
                ('nota_avaliacao', models.DecimalField(decimal_places=1, max_digits=3, max_length=10)),
                ('categoria', models.ManyToManyField(to='app.categoria')),
                ('diretor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.diretor')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pais')),
            ],
        ),
        migrations.CreateModel(
            name='Temporada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temporada', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Serie_Epsodio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epsodio', models.ManyToManyField(to='app.epsodio')),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.serie')),
                ('temporada', models.ManyToManyField(to='app.temporada')),
            ],
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('duracao', models.DecimalField(decimal_places=2, max_digits=7)),
                ('sinopse', models.CharField(max_length=255)),
                ('site', models.CharField(max_length=255)),
                ('data_lancamento', models.DateField(verbose_name='data_lancamento')),
                ('nota_avaliacao', models.DecimalField(decimal_places=1, max_digits=3, max_length=10)),
                ('categoria', models.ManyToManyField(to='app.categoria')),
                ('diretor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.diretor')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pais')),
            ],
        ),
        migrations.CreateModel(
            name='Elenco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ator', models.ManyToManyField(to='app.ator')),
                ('diretor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.diretor')),
                ('filme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.filme')),
            ],
        ),
    ]
