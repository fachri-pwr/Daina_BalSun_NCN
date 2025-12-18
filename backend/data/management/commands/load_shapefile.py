import geopandas as gpd
from sqlalchemy import create_engine
from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils import timezone  # Import this
import os

class Command(BaseCommand):
    help = 'Uploads a shapefile to PostGIS using GeoPandas and SQLAlchemy'

    def add_arguments(self, parser):
        parser.add_argument('--data-path', type=str, help='Path to the .shp file')
        parser.add_argument('--table-name', type=str, help='Target table name in Postgres')

    def handle(self, *args, **options):
        os.environ["SHAPE_RESTORE_SHX"] = "YES"
        data_path = options['data_path']
        table_name = options['table_name']

        if not data_path or not table_name:
            self.stderr.write("Error: Both --data-path and --table-name are required.")
            return

        db_config = settings.DATABASES['default']
        conn_str = (
            f"postgresql://{db_config['USER']}:{db_config['PASSWORD']}@"
            f"{db_config['HOST'] or 'localhost'}:{db_config['PORT'] or '5432'}/"
            f"{db_config['NAME']}"
        )

        try:
            self.stdout.write(self.style.SUCCESS(f"Reading: {data_path}"))
            gdf = gpd.read_file(data_path)

            if gdf.crs is None:
                gdf.set_crs(epsg=4326, inplace=True)
                self.stdout.write(self.style.WARNING("No CRS detected, defaulting to EPSG:4326"))

            # --- ADD TIMESTAMP HERE ---
            self.stdout.write("Adding upload timestamp...")
            # This creates a new column named 'created' and fills it with the current time
            gdf['created'] = timezone.now()
            # ---------------------------

            # Upload using SQLAlchemy engine
            engine = create_engine(conn_str)
            self.stdout.write(f"Uploading to table: {table_name}...")

            # Since if_exists='replace', the table will now include the 'created' column
            gdf.to_postgis(name=table_name, con=engine, if_exists='replace', index=False)

            self.stdout.write(self.style.SUCCESS(f"Successfully loaded data into {table_name} with timestamps!"))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Failed: {str(e)}"))