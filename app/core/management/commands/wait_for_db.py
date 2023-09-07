"""Django command to wait for db to be available
"""
from typing import Any
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write("Waiting for Database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Database unavailable. Waiting 1 second ...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database Available!"))
