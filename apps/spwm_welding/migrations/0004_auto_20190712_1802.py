# Generated by Django 2.2.2 on 2019-07-12 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spwm_welding', '0003_wps_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wps',
            name='Produto',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='wps',
            name='descricao',
            field=models.CharField(max_length=100),
        ),
    ]
