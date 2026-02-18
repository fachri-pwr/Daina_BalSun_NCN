from sqlalchemy import Column, Integer, String, Float, JSON
from database import Base

class FinalScore(Base):
    __tablename__ = "final_scores"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)
    
    # Required field
    box_id = Column(String, unique=True, index=True, nullable=False)

    # Optional Scores (matches your GeoJSON nulls)
    dni_score = Column(Float, nullable=True)
    pvout_score = Column(Float, nullable=True)
    temp_score = Column(Float, nullable=True)
    dem_score = Column(Float, nullable=True)
    dso_score = Column(Float, nullable=True)
    solar_score = Column(Float, nullable=True)
    station_score = Column(Float, nullable=True)
    road_score = Column(Float, nullable=True)
    
    # These were specific failures in your log
    land_score = Column(Float, nullable=True) 
    fclass = Column(String, nullable=True)


    # Metrics
    area = Column(Float, nullable=True)
    perimeter = Column(Float, nullable=True)
    region_name = Column(String, nullable=True)
    
    # rank 
    topsis_score=Column(Float, nullable=True)
    topsis_rank = Column(Float, nullable=True)

    # Geometry storage
    # If you haven't enabled PostGIS extension yet, keep this as JSON
    # If you HAVE enabled PostGIS, change this to Geometry(geometry_type='MULTIPOLYGON', srid=2180)
    geometry = Column(JSON, nullable=True)
    

class Boundary(Base):
    __tablename__ = "boundaries"

    id = Column(Integer, primary_key=True, index=True)
    # This stores "wroclaw"
    name = Column(String, unique=True, index=True, nullable=False)
    # This stores the geometry dict: {"type": "MultiPolygon", "coordinates": [...]}
    geometry = Column(JSON, nullable=False)