import os
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.utils import timezone
from data.models import *
from django.apps import apps


class Command(BaseCommand):
    help = 'Loads Box data from a fixture and updates the created timestamp afterward.'

    def add_arguments(self, parser):
        # This argument captures the path to your JSON fixture file
        parser.add_argument(
            "--app",
            type=str,
            required=True,
            help="App label (e.g. data)"
        )

        parser.add_argument(
            "--model",
            type=str,
            required=True,
            help="Model name (e.g. Box)"
        )

        parser.add_argument('--fixture-path', type=str, help='The path to the JSON fixture file.')

    def handle(self, *args, **options):
        app_label = options["app"]
        model_name = options["model"]
        fixture_path = options['fixture_path']

        # --- 1. Call the Standard 'loaddata' Command ---
        self.stdout.write(f'Attempting to load data from: {fixture_path}...')
        try:
            # We call the loaddata command using its standard behavior
            call_command('loaddata', fixture_path, verbosity=1)
            self.stdout.write(self.style.SUCCESS('Standard loaddata command finished successfully.'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error during loaddata: {e}'))
            return

        # --- 2. Run Your Custom Update Script ---

        self.stdout.write('Starting post-load timestamp update...')

        # Get the current time for the "upload date"
        now = timezone.now()

        # Find all Box objects where the created field is NULL
        # This targets the records just loaded by loaddata
        Model = apps.get_model(app_label, model_name)
        boxes_to_update = Model.objects.filter(created__isnull=True)

        # Use the .update() method to set the 'created' field
        updated_count = boxes_to_update.update(created=now)

        self.stdout.write(
            self.style.SUCCESS(f"Successfully updated {updated_count} Box objects with the created timestamp."))