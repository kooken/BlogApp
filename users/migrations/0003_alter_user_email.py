# Generated by Django 5.1.1 on 2024-09-12 14:33

import users.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[users.validators.validate_email_domain], verbose_name='email'),
        ),
    ]
