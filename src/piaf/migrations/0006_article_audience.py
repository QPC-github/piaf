# Generated by Django 2.2.6 on 2019-10-16 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piaf', '0005_paragraph_user_squashed_0006_auto_20191015_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='audience',
            field=models.CharField(choices=[('restricted', 'restricted'), ('all', 'all')], default='all', max_length=10),
            preserve_default=False,
        ),
    ]
