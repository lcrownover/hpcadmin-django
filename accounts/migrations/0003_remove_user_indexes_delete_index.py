# Generated by Django 4.1.4 on 2023-01-01 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_index_user_indexes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='indexes',
        ),
        migrations.DeleteModel(
            name='Index',
        ),
    ]
