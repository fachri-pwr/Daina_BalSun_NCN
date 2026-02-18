from pydantic import BaseModel, Field
from typing import List, Optional, Any, Union


# =========== Final score ============================
# 1. This matches the 'geometry' block
class Geometry(BaseModel):
    type: str  # e.g., "MultiPolygon"
    coordinates: List[Any] # Nested lists of floats

# 2. This matches the 'properties' block (All your scores)
class FinalScoreProperties(BaseModel):
    box_id: str
    dni_score: Optional[float] = None
    pvout_score: Optional[float] = None
    temp_score: Optional[float] = None
    dem_score: Optional[float] = None
    dso_score: Optional[float] = None
    solar_score: Optional[float] = None
    station_score: Optional[float] = None
    road_score: Optional[float] = None
    
    # These are the ones failing in your error log:
    land_score: Optional[float] = None  # Allows null/None
    fclass: Optional[str] = "unknown"   # Allows null, defaults to "unknown"
    area: Optional[float] = None
    perimeter: Optional[float] = None
    region_name: Optional[str] = None
    topsis_score : Optional[float] = None
    topsis_rank : Optional[int] = None

# 3. This matches a single 'Feature'
class FinalScoreFeature(BaseModel):
    type: str = "Feature"
    properties: FinalScoreProperties
    geometry: Geometry

# 4. This matches the 'crs' block in your file
class CRSProperties(BaseModel):
    name: str

class CRS(BaseModel):
    type: str
    properties: CRSProperties

# 5. This is the main schema for the whole File
class FinalScoreGeoJSONFeatureCollection(BaseModel):
    type: str = "FeatureCollection"
    name: Optional[str] = None
    crs: Optional[CRS] = None
    features: List[FinalScoreFeature]

    class Config:
        from_attributes = True
        

## boundary

class FeatureBoundary(BaseModel):
    type: str
    geometry: Geometry
    # We define properties as an empty dict or optional to avoid validation errors, 
    # but we won't use the data inside it.
    properties: dict
    
# 3. Define the Main FeatureCollection Model
class BoundaryFeatureCollection(BaseModel):
    name: str # Captures "wroclaw"
    features: List[FeatureBoundary]

    class Config:
        from_attributes = True
