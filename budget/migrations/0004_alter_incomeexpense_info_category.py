# Generated by Django 4.0.1 on 2022-01-14 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_rename_incomeexpense_incomeexpense_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomeexpense_info',
            name='category',
            field=models.CharField(choices=[('Jedzenie', 'Jedzenie'), ('Podróże', 'Podróże'), ('Zakupy', 'Zakupy'), ('Rachunki', 'Rachunki'), ('Rozrywka', 'Rozrywka'), ('Wpływ', 'Wpływ'), ('Inne', 'Inne')], default='Jedzenie', max_length=50),
        ),
    ]
