# Generated by Django 3.2 on 2022-02-14 02:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Logistics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Name_Route', models.CharField(max_length=100)),
                ('Code_ID_Route', models.CharField(max_length=100)),
                ('Phone', models.CharField(blank=True, max_length=50, verbose_name='Numero de telefono')),
                ('Comment', models.CharField(blank=True, max_length=500, null=True)),
                ('Company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.company')),
                ('Created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalRoutes',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('Name_Route', models.CharField(max_length=100)),
                ('Code_ID_Route', models.CharField(max_length=100)),
                ('Phone', models.CharField(blank=True, max_length=50, verbose_name='Numero de telefono')),
                ('Comment', models.CharField(blank=True, max_length=500, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('Company', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Company.company')),
                ('Created_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical routes',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
