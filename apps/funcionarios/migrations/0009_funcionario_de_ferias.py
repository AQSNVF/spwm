# Generated by Django 2.2.2 on 2019-06-27 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0008_funcionario_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='de_ferias',
            field=models.BooleanField(default=False),
        ),
    ]
