# Generated by Django 3.2 on 2022-02-14 03:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Product', '0007_equipment_warranty_historicalequipment_warranty'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalDefect',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('Defect_description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción')),
                ('Defect_date', models.DateField(blank=True, default='2020-01-01', null=True, verbose_name='Fecha de avería')),
                ('Defect_time', models.TimeField(blank=True, default='00:00:00', null=True, verbose_name='Hora de avería')),
                ('Defect_status', models.CharField(choices=[('Functional', 'Averiado'), ('Defective', 'Defectuoso')], default='Functional', max_length=50)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('ID_DistributionCenter', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Company.distributioncenter')),
                ('ID_Product', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Product.product')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Avería',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Defect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Defect_description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción')),
                ('Defect_date', models.DateField(blank=True, default='2020-01-01', null=True, verbose_name='Fecha de avería')),
                ('Defect_time', models.TimeField(blank=True, default='00:00:00', null=True, verbose_name='Hora de avería')),
                ('Defect_status', models.CharField(choices=[('Functional', 'Averiado'), ('Defective', 'Defectuoso')], default='Functional', max_length=50)),
                ('ID_DistributionCenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.distributioncenter')),
                ('ID_Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.product')),
            ],
            options={
                'verbose_name': 'Avería',
                'verbose_name_plural': 'Averías',
            },
        ),
    ]
