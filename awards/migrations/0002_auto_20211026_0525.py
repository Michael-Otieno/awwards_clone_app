# Generated by Django 3.2.8 on 2021-10-26 02:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='content_average',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='rating',
            name='design_average',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='rating',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='awards.project'),
        ),
        migrations.AddField(
            model_name='rating',
            name='score',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='rating',
            name='usability_average',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='content',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')]),
        ),
        migrations.AlterField(
            model_name='rating',
            name='design',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='usability',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')]),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rater', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set(),
        ),
        migrations.AlterIndexTogether(
            name='rating',
            index_together=set(),
        ),
        migrations.RemoveField(
            model_name='rating',
            name='project',
        ),
    ]
