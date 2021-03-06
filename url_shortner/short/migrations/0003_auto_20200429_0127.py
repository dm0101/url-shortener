# Generated by Django 3.0.5 on 2020-04-28 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0002_auto_20200429_0005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='clicks',
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('url_hash', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='short.URL', to_field='url_hash')),
            ],
        ),
    ]
