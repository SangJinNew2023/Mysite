# Generated by Django 4.1.6 on 2023-02-24 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("mysitev1", "0006_question_voter_alter_question_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="voter",
            field=models.ManyToManyField(
                related_name="voter_answer", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="answer",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="author_answer",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]