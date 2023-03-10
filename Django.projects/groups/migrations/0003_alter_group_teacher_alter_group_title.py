# Generated by Django 4.1.7 on 2023-03-08 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("groups", "0002_group_group_students_group_students_group_teacher"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="teacher",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="groups.teacher",
                verbose_name="Учителя",
            ),
        ),
        migrations.AlterField(
            model_name="group",
            name="title",
            field=models.CharField(max_length=100, verbose_name="Загаловок"),
        ),
    ]
