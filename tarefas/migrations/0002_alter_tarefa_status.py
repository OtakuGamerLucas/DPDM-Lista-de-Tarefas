# Generated by Django 4.0.5 on 2022-07-08 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='status',
            field=models.CharField(default='Ativa', max_length=9),
        ),
    ]
