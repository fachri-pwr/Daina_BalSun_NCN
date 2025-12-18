from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.apps import apps


class Command(BaseCommand):
    help = "Delete records from a Django model in batches"

    def add_arguments(self, parser):
        parser.add_argument("--app", type=str, required=True, help="App label (e.g. data)")
        parser.add_argument("--model", type=str, required=True, help="Model name (e.g. Landuse)")
        parser.add_argument("--batch-size", type=int, default=1000, help="Records per batch")

    def handle(self, *args, **options):
        app_label = options["app"]
        model_name = options["model"]
        batch_size = options["batch_size"]

        try:
            Model = apps.get_model(app_label, model_name)
        except LookupError:
            raise CommandError(f"Model '{app_label}.{model_name}' not found")

        self.stdout.write(
            self.style.WARNING(f"Deleting from {app_label}.{model_name} in batches of {batch_size}")
        )

        total_deleted = 0

        # Continue as long as there are records to delete
        while Model.objects.exists():
            with transaction.atomic():
                # 1. Use 'pk' to be compatible with any primary key name (id, osm_id, etc.)
                # 2. Convert result to a list of strings to avoid "text = integer" DB errors
                raw_ids = Model.objects.values_list("pk", flat=True)[:batch_size]
                ids = [str(pk_val) for pk_val in raw_ids]

                if not ids:
                    break

                # 3. Use pk__in with our string-converted list
                deleted_count, _ = Model.objects.filter(pk__in=ids).delete()
                total_deleted += deleted_count

                self.stdout.write(f"Deleted {total_deleted} records so far...")

        self.stdout.write(self.style.SUCCESS(f"Done. Total deleted: {total_deleted}"))