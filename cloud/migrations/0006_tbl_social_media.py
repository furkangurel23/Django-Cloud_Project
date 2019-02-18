# Generated by Django 2.1.4 on 2019-01-12 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0005_tbl_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_social_media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_type', models.CharField(max_length=50)),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloud.tbl_user', verbose_name='Owner')),
            ],
        ),
    ]