# Generated by Django 3.0.2 on 2020-01-29 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20200128_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(blank=True, max_length=20, null=True)),
                ('descricao', models.CharField(blank=True, max_length=70, null=True)),
            ],
        ),
    ]
