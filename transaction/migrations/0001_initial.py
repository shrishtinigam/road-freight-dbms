# Generated by Django 3.2.9 on 2021-11-26 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('wt_ore', models.FloatField()),
                ('type_ore', models.CharField(max_length=45)),
                ('from_dest', models.CharField(max_length=45)),
                ('to_dest', models.CharField(max_length=45)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField()),
                ('fastag', models.CharField(max_length=45)),
                ('status', models.CharField(max_length=45)),
                ('number_plate', models.CharField(max_length=45)),
                ('receiver_id', models.CharField(max_length=45)),
            ],
        ),
    ]