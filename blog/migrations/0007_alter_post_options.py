# Generated by Django 4.2.3 on 2023-08-04 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_rename_category_post_post_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-published_date"]},
        ),
    ]
