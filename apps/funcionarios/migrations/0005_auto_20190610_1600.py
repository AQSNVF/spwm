# Generated by Django 2.2.2 on 2019-06-10 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0004_auto_20190610_1020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='departamento',
            new_name='departamentos',
        ),
    ]