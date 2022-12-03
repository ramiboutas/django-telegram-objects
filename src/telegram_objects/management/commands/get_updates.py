from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from telegram_objects.api import create_update_objects
from telegram_objects.api import get_telegram_updates


class Command(BaseCommand):
    help = "Read last updates from Telegram and save them in the database."

    def handle(self, *args, **options):
        self.stdout.write("Updating...")
        get_updates_and_save_to_db()
        self.stdout.write("Done.")


@transaction.atomic
def get_updates_and_save_to_db():
    response_dict, ok = get_telegram_updates()
    if ok:
        create_update_objects(response_dict)
    else:
        print("getUpdates not ok") # TODO: improve error message