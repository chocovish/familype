# Generated by Django 2.1.5 on 2019-02-16 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20190216_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.CharField(choices=[('child', 'Child'), ('parent', 'Parent')], max_length=6),
        ),
    ]
