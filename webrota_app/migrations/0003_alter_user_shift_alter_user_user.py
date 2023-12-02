# Generated by Django 4.2.7 on 2023-11-12 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webrota_app", "0002_alter_user_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="shift",
            field=models.CharField(
                choices=[("Day", "Day"), ("Night", "Night")],
                default="",
                help_text="Select the shift time: Day or Night",
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="user",
            field=models.CharField(
                choices=[
                    ("User_A", "User_A"),
                    ("User_B", "User_B"),
                    ("User_C", "User_C"),
                    ("User_D", "User_D"),
                ],
                default="",
                help_text="Select user",
                max_length=100,
            ),
        ),
    ]