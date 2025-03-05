"""
This script will change the voicemail settings for a list of extensions loaded from a exported csv file, printing Time taken for each extension.
"""

import timeit
from selenium.webdriver import Firefox
from pilot.page_objects import FusionPBX
import csv
import secrets

password_length = 10


browser = Firefox()

url = "https://192.168.1.24"  # URL of your FusionPBX
user = "admin@pabx.antares.local"  # User with superadmin privileges
password = ""  # Password for the user


def set_password(exten):
    e = d.extension(exten)
    print(f"Setting  password {e.name}")
    e.password = secrets.token_urlsafe(password_length)


def read_from_csv(csv_file):
    with open(csv_file) as csv_extens:
        reader = csv.DictReader(csv_extens)
        for row in reader:
            print({row["extension"]}, row["password"])
            if not row["password"]:
                print("----------------------------------------------")
                print(f"Trying   {row['extension']}")
                set_password(row["extension"])
            else:
                print(f"Skipping {row['extension']}: {row['password']}")


f = FusionPBX(browser, url, user, password)
d = f.domain("pabx.antares.local")
# extensions = d.extensions
# print(extensions)
read_from_csv("samples/csv/extension_export_2024-04-11.csv")
