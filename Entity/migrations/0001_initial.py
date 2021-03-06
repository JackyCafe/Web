# Generated by Django 2.1.7 on 2019-03-04 05:20

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date1', models.DateField(default=django.utils.timezone.now)),
                ('entity', models.CharField(max_length=200)),
                ('lot_no', models.CharField(blank=True, max_length=20, null=True)),
                ('current_status', models.TextField(blank=True, null=True)),
                ('status_history', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-date1',),
            },
            managers=[
                ('obj', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='OrderLot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lot_no', models.CharField(blank=True, max_length=20, null=True, verbose_name='批號')),
                ('entity', models.CharField(blank=True, max_length=20, null=True, verbose_name='機台')),
                ('current_status', models.CharField(blank=True, max_length=200, null=True, verbose_name='現況')),
                ('product_status', models.CharField(blank=True, max_length=200, null=True, verbose_name='現況')),
                ('finish', models.BooleanField(default=False, verbose_name='採收')),
            ],
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date1', models.DateField(default=django.utils.timezone.now)),
                ('order_no', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('-date1',),
            },
        ),
        migrations.AddField(
            model_name='orderlot',
            name='order_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Entity.WorkOrder'),
        ),
    ]
