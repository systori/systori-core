# Generated by Django 3.0.3 on 2020-02-09 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20200209_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Reihenfolge'),
            preserve_default=False,
        ),
    ]
