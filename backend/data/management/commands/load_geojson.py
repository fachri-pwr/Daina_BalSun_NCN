import geopandas as gpd
from sqlalchemy import create_engine,text
from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils import timezone # 1. Import timezone
from data.models import *
#
#
class Command(BaseCommand):
    help = 'Uploads a GeoJSON file to PostGIS using GeoPandas and SQLAlchemy'

    def add_arguments(self, parser):
        parser.add_argument('--data-path', type=str, help='Path to the .json or .geojson file')
        parser.add_argument('--table-name', type=str, help='Target table name in Postgres')

    def handle(self, *args, **options):
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
            self.stdout.write(self.style.SUCCESS(f"Reading GeoJSON: {data_path}"))
            gdf = gpd.read_file(data_path)

            if gdf.crs is None:
                gdf.set_crs(epsg=2180, inplace=True)
                self.stdout.write(self.style.WARNING("No CRS detected, defaulting to EPSG:4326"))

            # --- DYNAMIC ID HANDLING ---
            # Find all columns that contain 'id' (case-insensitive)
            id_columns = [col for col in gdf.columns if 'id' in col.lower()]

            for col in id_columns:
                self.stdout.write(f"Ensuring ID column '{col}' is string format...")
                gdf[col] = gdf[col].astype(str)
            # ---------------------------

            # --- 2. ADD TIMESTAMP HERE ---
            self.stdout.write("Adding upload timestamp...")
            gdf['created'] = timezone.now()
            # ---------------------------

            engine = create_engine(conn_str)
            self.stdout.write(f"Uploading to table: {table_name}...")

            # 1. Drop 'id' from the DataFrame if it exists to avoid conflicts
            if 'id' in gdf.columns:
                gdf = gdf.drop(columns=['id'])

            # 2. Upload using index=False
            gdf.to_postgis(
                name=table_name,
                con=engine,
                if_exists='append',  # Keep old data
                index=False  # Do NOT create a column from the DataFrame index
            )

            self.stdout.write(self.style.SUCCESS(f"Successfully loaded GeoJSON into {table_name} with timestamps!"))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Failed: {str(e)}"))





# class Command(BaseCommand):
#     help = 'Uploads a GeoJSON file to PostGIS with custom ID logic'
#
#     def add_arguments(self, parser):
#         parser.add_argument('--data-path', type=str, help='Path to the .json or .geojson file')
#         parser.add_argument('--table-name', type=str, help='Target table name in Postgres')
#
#     def handle(self, *args, **options):
#         data_path = options['data_path']
#         table_name = options['table_name']
#
#         if not data_path or not table_name:
#             self.stderr.write("Error: Both --data-path and --table-name are required.")
#             return
#
#         db_config = settings.DATABASES['default']
#         conn_str = (
#             f"postgresql://{db_config['USER']}:{db_config['PASSWORD']}@"
#             f"{db_config['HOST'] or 'localhost'}:{db_config['PORT'] or '5432'}/"
#             f"{db_config['NAME']}"
#         )
#         engine = create_engine(conn_str)
#
#         try:
#             self.stdout.write(self.style.SUCCESS(f"Reading GeoJSON: {data_path}"))
#             gdf = gpd.read_file(data_path)
#
#             if gdf.crs is None:
#                 gdf.set_crs(epsg=4326, inplace=True)
#
#             # 1. HANDLE PRIMARY KEY (osm_map_id)
#             prefix = "id"
#
#             # Get the current max ID from the database to continue the sequence
#             # We use SQLAlchemy to query the table directly
#             with engine.connect() as conn:
#                 query = text(f"SELECT osm_map_id FROM {table_name} WHERE osm_map_id LIKE '{prefix}%'")
#                 existing_ids = [row[0] for row in conn.execute(query).fetchall()]
#
#             # Determine starting numeric suffix
#             if existing_ids:
#                 # Extract numbers from strings like 'id1', 'id2' and find max
#                 numeric_parts = [int(idx.replace(prefix, '')) for idx in existing_ids if
#                                  idx.replace(prefix, '').isdigit()]
#                 max_id = max(numeric_parts) if numeric_parts else 0
#             else:
#                 max_id = 0
#
#             # Generate new IDs for the incoming GeoJSON rows
#             self.stdout.write(f"Generating new IDs starting from {prefix}{max_id + 1}...")
#             gdf['osm_map_id'] = [f"{prefix}{max_id + i + 1}" for i in range(len(gdf))]
#
#             # 2. ADD TIMESTAMP
#             gdf['created'] = timezone.now()
#
#             # 3. CLEANUP
#             # Ensure we don't have a column named 'id' which might conflict with Django/Postgres defaults
#             if 'id' in gdf.columns:
#                 gdf = gdf.drop(columns=['id'])
#
#             # 4. UPLOAD
#             self.stdout.write(f"Uploading {len(gdf)} rows to {table_name}...")
#             gdf.to_postgis(
#                 name=table_name,
#                 con=engine,
#                 if_exists='append',
#                 index=False
#             )
#
#             self.stdout.write(self.style.SUCCESS("Successfully loaded data with prefixed IDs!"))
#
#         except Exception as e:
#             self.stderr.write(self.style.ERROR(f"Failed: {str(e)}"))