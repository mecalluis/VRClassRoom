# Generated by Django 3.2 on 2022-04-04 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vroom', '0004_merge_0003_auto_20220317_1752_0003_auto_20220322_1052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipo_ejercicio',
            name='icono',
        ),
        migrations.AddField(
            model_name='documento',
            name='fecha_publicacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='ejercicio',
            name='fecha_publicacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='ejercicio',
            name='min_exercise_version',
            field=models.FloatField(blank=True, default=1.0, null=True),
        ),
        migrations.AddField(
            model_name='entrega',
            name='fecha_calificacion',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='entrega',
            name='profesor',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='profesor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='link',
            name='fecha_publicacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='texto',
            name='fecha_publicacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='centro',
            name='icono',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='ejercicio',
            name='descripcion',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='entrega',
            name='archivo',
            field=models.FileField(blank=True, default=None, null=True, upload_to='static/assets/archivos'),
        ),
        migrations.AlterField(
            model_name='entrega',
            name='comentario_alumno',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='entrega',
            name='comentario_profesor',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='entrega',
            name='fecha_edicion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='entrega',
            name='fecha_publicacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(default=None, max_length=4, unique=True)),
                ('ejercicio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vroom.ejercicio')),
                ('usuario', models.ForeignKey(default=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
