from sqlalchemy.orm import Session
import models, schemas

def create_finalscore_geojson_features(db: Session, geo_data: schemas.FinalScoreGeoJSONFeatureCollection):
    """
    Takes the validated GeoJSON data and dumps it into the PostgreSQL database.
    """
    db_records = []

    for feature in geo_data.features:
        # 1. Extract properties and geometry from the Pydantic model
        props = feature.properties
        geom = feature.geometry.model_dump() # Convert Geometry object to a dict for JSON column

        # 2. Create the model instance
        db_record = models.FinalScore(
            box_id=props.box_id,
            dni_score=props.dni_score,
            pvout_score=props.pvout_score,
            temp_score=props.temp_score,
            dem_score=props.dem_score,
            dso_score=props.dso_score,
            solar_score=props.solar_score,
            station_score=props.station_score,
            road_score=props.road_score,
            land_score=props.land_score,
            fclass=props.fclass,
            area=props.area,
            perimeter=props.perimeter,
            region_name=props.region_name,
            topsis_score = props.topsis_score,
            topsis_rank = props.topsis_rank,
            geometry=geom
        )
        db_records.append(db_record)

    # 3. Use add_all for better performance than adding one-by-one
    db.add_all(db_records)
    
    try:
        db.commit()
        # Optional: Refreshing many records is slow, so we just return the count
        return len(db_records)
    except Exception as e:
        db.rollback()
        raise e

def get_all_final_scores(db: Session):
    return db.query(models.FinalScore).all()

def get_final_score_by_box_region(db: Session, region_name: str):
    return db.query(models.FinalScore).filter(models.FinalScore.region_name== region_name).all()


## ==== boudary
def create_boundary_features(db: Session, data: schemas.BoundaryFeatureCollection):
    # 1. Get name from the top level of the GeoJSON (e.g., 'wroclaw')
    city_name = data.name 
    
    # 2. Get the geometry from the first feature in the list
    # Assuming one feature per file, otherwise loop through data.features
    first_feature = data.features[0]
    
    new_boundary = models.Boundary(
        name=city_name,
        geometry=first_feature.geometry.dict() # Stores the MultiPolygon dict
    )
    
    db.add(new_boundary)
    db.commit()
    db.refresh(new_boundary)
    return 1 # Returns count of 1 feature imported

def get_boundary_by_region(db: Session, region_name: str):
    return db.query(models.Boundary).filter(models.Boundary.name== region_name).first()