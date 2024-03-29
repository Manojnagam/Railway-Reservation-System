# Generated by Django 4.2 on 2023-04-28 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0007_auto_20230428_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='phone_number',
            field=models.IntegerField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='trains',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
