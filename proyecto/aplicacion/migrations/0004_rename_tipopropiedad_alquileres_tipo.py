# Generated by Django 4.2.3 on 2023-08-13 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_rename_tipopropiedad_venta_tipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alquileres',
            old_name='tipoPropiedad',
            new_name='tipo',
        ),
    ]
