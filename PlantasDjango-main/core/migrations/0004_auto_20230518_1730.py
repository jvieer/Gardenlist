# Generated by Django 3.1.2 on 2023-05-18 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_auto_20230518_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarroCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCarro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.carrocompra')),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.PositiveIntegerField(),
        ),
        migrations.DeleteModel(
            name='Carro',
        ),
        migrations.AddField(
            model_name='itemcarro',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto'),
        ),
        migrations.AddField(
            model_name='carrocompra',
            name='productos',
            field=models.ManyToManyField(through='core.ItemCarro', to='core.Producto'),
        ),
        migrations.AddField(
            model_name='carrocompra',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
