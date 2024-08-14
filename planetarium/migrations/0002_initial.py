# Generated by Django 5.0.8 on 2024-08-07 09:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("planetarium", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="showsession",
            name="astronomy_show",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ShowSessions",
                to="planetarium.astronomyshow",
            ),
        ),
        migrations.AddField(
            model_name="showsession",
            name="planetarium_dome",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ShowSessions",
                to="planetarium.planetariumdome",
            ),
        ),
        migrations.AddField(
            model_name="astronomyshow",
            name="show_theme",
            field=models.ManyToManyField(to="planetarium.showtheme"),
        ),
        migrations.AddField(
            model_name="ticket",
            name="reservation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tickets",
                to="planetarium.reservation",
            ),
        ),
        migrations.AddField(
            model_name="ticket",
            name="show_session",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tickets",
                to="planetarium.showsession",
            ),
        ),
    ]
