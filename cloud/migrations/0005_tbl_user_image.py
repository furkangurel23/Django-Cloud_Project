# Generated by Django 2.1.4 on 2019-01-11 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0004_tbl_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_user',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]