# Generated by Django 3.2.7 on 2021-09-11 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(max_length=4, verbose_name='Код страны')),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_value', models.DateField(verbose_name='Дата')),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmed', models.IntegerField(verbose_name='Подтвержденные случаи')),
                ('deaths', models.IntegerField(verbose_name='Количество смертей')),
                ('stringency_actual', models.IntegerField(verbose_name='Актуальный уровень ограничений')),
                ('stringency', models.IntegerField(verbose_name='Уровень ограничений')),
                ('country_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='death_table.country')),
                ('date_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='death_table.date')),
            ],
        ),
    ]
