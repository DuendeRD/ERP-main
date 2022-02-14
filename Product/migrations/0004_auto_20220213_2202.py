# Generated by Django 3.2 on 2022-02-14 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_historicalproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproduct',
            name='Status',
            field=models.CharField(choices=[('Functional', 'Averiado')], default='Functional', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='Status',
            field=models.CharField(choices=[('Functional', 'Averiado')], default='Functional', max_length=50),
        ),
    ]