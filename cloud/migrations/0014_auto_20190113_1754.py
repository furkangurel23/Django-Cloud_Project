# Generated by Django 2.1.4 on 2019-01-13 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0013_auto_20190113_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_image',
            name='image_id',
        ),
        migrations.AlterField(
            model_name='tbl_image',
            name='tbl_file_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cloud.tbl_file'),
        ),
    ]
