# Generated by Django 5.0.7 on 2024-07-16 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$720000$ykhH5BBRQGqdipAEwiGyE5$EvW9m1XpIzvdO2CapjvKcd4DvRZZ4TO+NVFrYx85rE8=', max_length=128),
        ),
    ]
