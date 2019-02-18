# Generated by Django 2.1.4 on 2019-01-12 17:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0009_tbl_external_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_share_external',
            fields=[
                ('share_id', models.AutoField(primary_key=True, serialize=False)),
                ('expire_on', models.DateField(default=django.utils.timezone.now)),
                ('file_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloud.tbl_file', verbose_name='File Name')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloud.tbl_external_user', verbose_name='User Name')),
            ],
        ),
    ]
