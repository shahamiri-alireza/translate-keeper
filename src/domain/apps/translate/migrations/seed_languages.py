from django.db import migrations
import csv
import os


def load_language_data(apps, schema_editor):
    Language = apps.get_model("translate", "Language")

    csv_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "statics", "languages.csv"
    )

    with open(csv_file_path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            Language.objects.create(
                name=row["English Name"],
                native_name=row["Native Name"],
                abbreviation=row["Abbreviation"],
                rtl=row["RTL"] == "true",
            )


class Migration(migrations.Migration):
    dependencies = [
        ("translate", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(load_language_data),
    ]
