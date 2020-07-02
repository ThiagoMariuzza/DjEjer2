# Generated by Django 2.2 on 2020-07-02 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ventas',
            name='id_producto',
        ),
        migrations.CreateModel(
            name='Detelles_Venta',
            fields=[
                ('id_detalle', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Producto')),
            ],
        ),
        migrations.AddField(
            model_name='ventas',
            name='id_detalle',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tienda.Detelles_Venta'),
        ),
    ]