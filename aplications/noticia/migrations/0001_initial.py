# Generated by Django 4.1.4 on 2022-12-22 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo')),
                ('fecha_noticia', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='noticia')),
                ('subtitulo_detalles', models.CharField(max_length=100, verbose_name='Subtitulo')),
                ('texto', models.TextField(max_length=2000, verbose_name='Texto')),
                ('categorias', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categorias', to='categorias.categorias')),
            ],
        ),
    ]