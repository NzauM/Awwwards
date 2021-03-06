# Generated by Django 2.0 on 2020-01-13 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ratings', '0002_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.IntegerField(default=1)),
                ('usabilty', models.IntegerField(default=1)),
                ('content', models.IntegerField(default=1)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ratings.Projects')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
