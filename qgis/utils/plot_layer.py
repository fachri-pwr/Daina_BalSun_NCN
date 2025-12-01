import geopandas as gpd
import geoplot as gplt
import geoplot.crs as gcrs
import matplotlib.pyplot as plt

gdf = gpd.read_file("../output/clipped_result_1.geojson")

# Make sure CRS is known, then convert to lat/lon
if gdf.crs is None:
    gdf = gdf.set_crs(epsg=2180)   # if you know it's EPSG:2180
gdf_ll = gdf.to_crs(epsg=4326)     # WGS84 lon/lat

# Use a simple PlateCarree (lon/lat) map
ax = gplt.polyplot(
    gdf_ll,
    projection=gcrs.PlateCarree(),
    edgecolor='darkgrey',
    facecolor='lightgrey',
    linewidth=0.3,
    figsize=(12, 8),
)
plt.title("Clipped Grid (EPSG:2180 → EPSG:4326)")
plt.show()
