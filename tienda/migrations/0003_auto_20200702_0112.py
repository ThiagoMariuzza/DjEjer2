# Generated by Django 2.2 on 2020-07-02 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_auto_20200702_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id_producto',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
    ]