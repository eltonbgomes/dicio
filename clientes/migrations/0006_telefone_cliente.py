# Generated by Django 3.0.2 on 2020-01-29 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20200128_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='telefone',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente'),
            preserve_default=False,
        ),
    ]