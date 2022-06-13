"""
Django command to wait for Database to start;
"""
# noinspection PyUnresolvedReferences
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for Database"""

    def handle(self, *args, **options):
        pass
