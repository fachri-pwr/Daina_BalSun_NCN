# import os
# import re
# import zipfile
# import xml.etree.ElementTree as ET
# from typing import Optional, List, Tuple
# import sys


# # Point Shapely to GEOS inside the QGIS app bundle (you found this path)
# os.environ["SHAPELY_LIBRARY_PATH"] = "/Applications/QGIS-LTR.app/Contents/MacOS/lib/libgeos_c.dylib"

# # Point PROJ and GDAL data to QGIS bundle
# os.environ["PROJ_LIB"] = "/Applications/QGIS-LTR.app/Contents/Resources/proj"
# os.environ["GDAL_DATA"] = "/Applications/QGIS-LTR.app/Contents/Resources/gdal"

# # Help macOS dynamic loader find QGIS libraries
# os.environ["DYLD_FALLBACK_LIBRARY_PATH"] = "/Applications/QGIS-LTR.app/Contents/MacOS/lib:" + os.environ.get(
#     "DYLD_FALLBACK_LIBRARY_PATH", "")

# # Add QGIS Python paths (keep these before importing QGIS/geopandas)
# PYTHON_PATH = "/Applications/QGIS-LTR.app/Contents/Resources/python"
# PLUGIN_PATH = "/Applications/QGIS-LTR.app/Contents/Resources/python/plugins"
# SITE_PACKAGES = "/Applications/QGIS-LTR.app/Contents/MacOS/lib/python3.9/site-packages"
# sys.path[:0] = [PYTHON_PATH, PLUGIN_PATH, SITE_PACKAGES]  # prepend to avoid accidental shadowing

# KML_NS = {"kml": "http://www.opengis.net/kml/2.2"}

# import geopandas as gpd
# from shapely.geometry import Point, LineString, Polygon
# from shapely.geometry.base import BaseGeometry

# # ---------- helpers ----------
# def read_kml_from_kmz(kmz_path: str) -> bytes:
#     with zipfile.ZipFile(kmz_path, "r") as z:
#         for cand in ("doc.kml", "kml/doc.kml", "Doc.kml"):
#             try:
#                 return z.read(cand)
#             except KeyError:
#                 pass
#         for name in z.namelist():
#             if name.lower().endswith(".kml"):
#                 return z.read(name)
#     raise FileNotFoundError("No .kml file found inside KMZ.")

# def iter_container(elem, path: Optional[List[str]] = None):
#     if path is None:
#         path = []
#     for e in list(elem):
#         tag = e.tag.split("}")[-1]
#         if tag in ("Folder", "Document"):
#             nm = e.findtext("kml:name", default="", namespaces=KML_NS)
#             yield from iter_container(e, path + [nm])
#         elif tag == "Placemark":
#             yield path, e

# def coords_text_to_xylist(text: str) -> List[Tuple[float, float]]:
#     pts: List[Tuple[float, float]] = []
#     if not text:
#         return pts
#     for token in text.strip().split():
#         parts = token.split(",")
#         if len(parts) >= 2:
#             try:
#                 pts.append((float(parts[0]), float(parts[1])))
#             except ValueError:
#                 continue
#     return pts

# def placemark_to_record(path: List[str], pm) -> Optional[dict]:
#     name = pm.findtext("kml:name", default=None, namespaces=KML_NS)
#     desc = pm.findtext("kml:description", default=None, namespaces=KML_NS)
#     folder = "/".join([p for p in path if p])

#     geom = None
#     el = pm.find(".//kml:Point/kml:coordinates", KML_NS)
#     if el is not None and el.text:
#         pts = coords_text_to_xylist(el.text)
#         if pts:
#             geom = Point(pts[0])

#     if geom is None:
#         el = pm.find(".//kml:LineString/kml:coordinates", KML_NS)
#         if el is not None and el.text:
#             pts = coords_text_to_xylist(el.text)
#             if len(pts) >= 2:
#                 geom = LineString(pts)

#     if geom is None:
#         el = pm.find(".//kml:Polygon/kml:outerBoundaryIs//kml:coordinates", KML_NS)
#         if el is not None and el.text:
#             ring = coords_text_to_xylist(el.text)
#             if len(ring) >= 3:
#                 geom = Polygon(ring)

#     if not isinstance(geom, BaseGeometry):
#         return None

#     rec = {"folder": folder, "name": name, "description": desc, "geometry": geom}

#     ext = pm.find("kml:ExtendedData", KML_NS)
#     if ext is not None:
#         for d in ext.findall("kml:Data", KML_NS):
#             n = d.attrib.get("name")
#             v = d.findtext("kml:value", default=None, namespaces=KML_NS)
#             if n:
#                 rec[n] = v
#         for sd in ext.findall(".//kml:SimpleData", KML_NS):
#             n = sd.attrib.get("name")
#             if n:
#                 rec[n] = sd.text
#     return rec

# def extract_city(folder: str, operator_name: str) -> Optional[str]:
#     """Extract city from '.../OSD/<operator>/[optional]/<City>/stacje'."""
#     if not isinstance(folder, str):
#         return None
#     op_pat = re.escape(operator_name)
#     m = re.search(fr"/{op_pat}/(?:[^/]+/)?([^/]+)/stacje", folder, flags=re.IGNORECASE)
#     return m.group(1) if m else None

# def to_ascii_safe(s: Optional[str]) -> Optional[str]:
#     if s is None:
#         return None
#     try:
#         from unidecode import unidecode
#         return unidecode(s)
#     except Exception:
#         import unicodedata
#         return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")

# # ---------- main function ----------
# def extract_data(kmz_path: str, out_path: str, operator_name: str) -> str:
#     """
#     Parse KMZ, filter '/OSD/<operator_name>/.../Stacje', convert non-points to centroids,
#     add 'substation_id' as a sequential ID (also set as index name),
#     and write ONE GeoJSON to `out_path` (WGS84). Returns out_path.
#     """
#     if not os.path.isfile(kmz_path):
#         raise FileNotFoundError(f"KMZ not found: {kmz_path}")

#     out_dir = os.path.dirname(out_path)
#     if out_dir:
#         os.makedirs(out_dir, exist_ok=True)

#     # Parse KML
#     kml_bytes = read_kml_from_kmz(kmz_path)
#     root = ET.fromstring(kml_bytes)

#     # Collect placemark records
#     records: List[dict] = []
#     for path, pm in iter_container(root, []):
#         rec = placemark_to_record(path, pm)
#         if rec:
#             records.append(rec)
#     if not records:
#         raise ValueError("No geometries parsed from KML.")

#     # Build GDF (WGS84)
#     gdf = gpd.GeoDataFrame(records, geometry="geometry", crs="EPSG:4326")

#     # Filter for /OSD/<operator>/ ... /Stacje   (case-insensitive)
#     folder_series = gdf["folder"].fillna("")
#     op_pat = re.escape(operator_name)
#     mask = (
#         folder_series.str.contains(fr"/OSD/{op_pat}/", case=False, na=False)
#         & folder_series.str.contains(r"/Stacje", case=False, na=False)
#     )
#     subset = gdf.loc[mask].copy()
#     if subset.empty:
#         raise ValueError(f"No features matched operator='{operator_name}' and 'Stacje' in folders.")

#     # Convert non-points to centroids in metric CRS for accuracy
#     metric = subset.to_crs(2180)
#     is_point = metric.geometry.geom_type == "Point"
#     metric.loc[~is_point, "geometry"] = metric.loc[~is_point, "geometry"].centroid
#     subset = metric.to_crs(4326)

#     # Add lon/lat and city
#     subset.loc[:, "x"] = subset.geometry.x
#     subset.loc[:, "y"] = subset.geometry.y
#     subset.loc[:, "city"] = subset["folder"].apply(lambda f: extract_city(f, operator_name))
#     subset.loc[:, "city_ascii"] = subset["city"].apply(to_ascii_safe)

#     # ensure clean ID column and avoid index-name collision
#     subset = subset.reset_index(drop=True)
#     subset["id"] = subset.index.astype(int)
#     subset.index.name = None  # <-- prevents GeoPandas from inserting index as 'substation_id'

#     subset.to_file(out_path, driver="GeoJSON") 
#     return subset

# # ---------- zero-arg runner (edit defaults here if you want) ----------
# if __name__ == "__main__":
#     KMZ_PATH = "../../data/input/dolnoslaskie/KSE_2019.kmz"
#     OUT_PATH = "../../data/output/dolnoslaskie/tauron_centroid.geojson"
#     OPERATOR  = "tauron"   # e.g., "tauron", "enea", "pge", etc.
#     # saved = extract_data(KMZ_PATH, OUT_PATH, OPERATOR)
#     # print("Saved GeoJSON:", saved)
#     extract_data(KMZ_PATH, OUT_PATH, OPERATOR)
#     print("Saved GeoJSON:")
 


import os
import re
import zipfile
import xml.etree.ElementTree as ET
from typing import Optional, List, Tuple
import sys

# We removed the sys.path hacks that cause the Python 3.12 vs 3.9 conflict.
import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon
from shapely.geometry.base import BaseGeometry

KML_NS = {"kml": "http://www.opengis.net/kml/2.2"}

# ---------- Helper Functions ----------

def read_kml_from_kmz(kmz_path: str) -> bytes:
    with zipfile.ZipFile(kmz_path, "r") as z:
        for cand in ("doc.kml", "kml/doc.kml", "Doc.kml"):
            try:
                return z.read(cand)
            except KeyError:
                pass
        for name in z.namelist():
            if name.lower().endswith(".kml"):
                return z.read(name)
    raise FileNotFoundError("No .kml file found inside KMZ.")

def iter_container(elem, path: Optional[List[str]] = None):
    if path is None:
        path = []
    for e in list(elem):
        tag = e.tag.split("}")[-1]
        if tag in ("Folder", "Document"):
            nm = e.findtext("kml:name", default="", namespaces=KML_NS)
            yield from iter_container(e, path + [nm])
        elif tag == "Placemark":
            yield path, e

def coords_text_to_xylist(text: str) -> List[Tuple[float, float]]:
    pts = []
    if not text: return pts
    for token in text.strip().split():
        parts = token.split(",")
        if len(parts) >= 2:
            try:
                pts.append((float(parts[0]), float(parts[1])))
            except ValueError:
                continue
    return pts

def placemark_to_record(path: List[str], pm) -> Optional[dict]:
    name = pm.findtext("kml:name", default=None, namespaces=KML_NS)
    desc = pm.findtext("kml:description", default=None, namespaces=KML_NS)
    folder = "/".join([p for p in path if p])

    geom = None
    el = pm.find(".//kml:Point/kml:coordinates", KML_NS)
    if el is not None and el.text:
        pts = coords_text_to_xylist(el.text)
        if pts: geom = Point(pts[0])

    if geom is None:
        el = pm.find(".//kml:LineString/kml:coordinates", KML_NS)
        if el is not None and el.text:
            pts = coords_text_to_xylist(el.text)
            if len(pts) >= 2: geom = LineString(pts)

    if geom is None:
        el = pm.find(".//kml:Polygon/kml:outerBoundaryIs//kml:coordinates", KML_NS)
        if el is not None and el.text:
            ring = coords_text_to_xylist(el.text)
            if len(ring) >= 3: geom = Polygon(ring)

    if not isinstance(geom, BaseGeometry):
        return None

    rec = {"folder": folder, "name": name, "description": desc, "geometry": geom}
    ext = pm.find("kml:ExtendedData", KML_NS)
    if ext is not None:
        for d in ext.findall("kml:Data", KML_NS):
            n = d.attrib.get("name")
            v = d.findtext("kml:value", default=None, namespaces=KML_NS)
            if n: rec[n] = v
        for sd in ext.findall(".//kml:SimpleData", KML_NS):
            n = sd.attrib.get("name")
            if n: rec[n] = sd.text
    return rec

def to_ascii_safe(s: Optional[str]) -> Optional[str]:
    if s is None: return None
    try:
        from unidecode import unidecode
        return unidecode(s)
    except Exception:
        import unicodedata
        return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")

def extract_operator_and_city(folder: str) -> Tuple[Optional[str], Optional[str]]:
    if not isinstance(folder, str):
        return None, None
    match = re.search(r"/OSD/([^/]+)/.*?([^/]+)/stacje", folder, flags=re.IGNORECASE)
    if match:
        return match.group(1), match.group(2)
    return None, None

# ---------- Main Logic ----------

def extract_all_dso_data(kmz_path: str, out_path: str):
    if not os.path.isfile(kmz_path):
        raise FileNotFoundError(f"KMZ not found: {kmz_path}")

    kml_bytes = read_kml_from_kmz(kmz_path)
    root = ET.fromstring(kml_bytes)

    records = []
    for path, pm in iter_container(root, []):
        rec = placemark_to_record(path, pm)
        if rec:
            records.append(rec)
    
    if not records:
        raise ValueError("No data found in KML.")

    gdf = gpd.GeoDataFrame(records, geometry="geometry", crs="EPSG:4326")

    folder_series = gdf["folder"].fillna("")
    mask = (
        folder_series.str.contains(r"/OSD/", case=False, na=False) & 
        folder_series.str.contains(r"/Stacje", case=False, na=False)
    )
    subset = gdf.loc[mask].copy()

    if subset.empty:
        print("No DSO stations found matching the folder pattern.")
        return

    extracted = subset["folder"].apply(extract_operator_and_city)
    subset["operator"] = extracted.apply(lambda x: x[0])
    subset["city"] = extracted.apply(lambda x: x[1])
    subset["city_ascii"] = subset["city"].apply(to_ascii_safe)

    # Use 2180 for Poland centroids
    metric = subset.to_crs(2180)
    is_point = metric.geometry.geom_type == "Point"
    metric.loc[~is_point, "geometry"] = metric.loc[~is_point, "geometry"].centroid
    subset = metric.to_crs(4326)

    subset["x"] = subset.geometry.x
    subset["y"] = subset.geometry.y
    subset = subset.reset_index(drop=True)
    subset["id"] = subset.index.astype(int)
    subset.index.name = None

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    subset.to_file(out_path, driver="GeoJSON")
    return subset

if __name__ == "__main__":
    KMZ_FILE = "/Users/sell/SynologyDrive/Dataset/daina/raw/global/DSO_KSE_2019.kmz"
    OUTPUT_FILE = "/Users/sell/SynologyDrive/Dataset/daina/raw/global/all_operators_dso.geojson"
    
    df = extract_all_dso_data(KMZ_FILE, OUTPUT_FILE)
    
    if df is not None:
        print(f"Extraction complete! Saved to: {OUTPUT_FILE}")
        print("Found operators:", df['operator'].unique())
        
        