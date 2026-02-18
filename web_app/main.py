from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List

import models, schemas, services
from database import engine, get_db

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="GeoSpatial Score API")

@app.post("/geojson/upload_finalscore", status_code=status.HTTP_201_CREATED)
async def upload_geojson_data(
    data: schemas.FinalScoreGeoJSONFeatureCollection, 
    db: Session = Depends(get_db)
):
    """
    Upload a complete GeoJSON FeatureCollection and save all features to Postgres.
    """
    try:
        count = services.create_finalscore_geojson_features(db, data)
        return {"message": f"Successfully imported {count} features"}
    except Exception as e:
        raise HTTPException(
            status_code=400, 
            detail=f"Database insertion failed: {str(e)}"
        )
        

@app.get("/geojson/all/final_score")
async def get_all_as_geojson(region_name:str | None=None,db: Session = Depends(get_db)):
    results = services.get_all_final_scores(db)
    return JSONResponse(content=jsonable_encoder(results))

@app.get("/geojson/all/final_score/{region_name}")
async def get_all_as_geojson_by_regionName(region_name:str,db: Session = Depends(get_db)):
    results = services.get_final_score_by_box_region(db, region_name)
    return JSONResponse(content=jsonable_encoder(results))

# @app.get("/scores/", response_model=List[schemas.FeatureProperties])
# async def read_all_scores(db: Session = Depends(get_db)):
#     """
#     Retrieve the properties of all stored spatial boxes.
#     """
#     scores = services.get_all_scores(db)
#     return scores

# @app.get("/scores/{box_id}", response_model=schemas.FeatureProperties)
# async def read_score_by_id(box_id: str, db: Session = Depends(get_db)):
#     """
#     Search for a specific box by its unique box_id.
#     """
#     db_score = services.get_score_by_box_id(db, box_id)
#     if db_score is None:
#         raise HTTPException(status_code=404, detail="Box ID not found")
#     return db_score


## boundary
@app.post("/geojson/upload_boundary", status_code=status.HTTP_201_CREATED)
async def upload_geojson_data(
    data: schemas.BoundaryFeatureCollection, 
    db: Session = Depends(get_db)
):
    try:
        # USE THE NEW SERVICE HERE
        count = services.create_boundary_features(db, data)
        return {"message": f"Successfully imported {count} features for {data.name}"}
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=400, 
            detail=f"Database insertion failed: {str(e)}"
        )

@app.get("/geojson/all/boundary/{region_name}")
async def get_boundary_by_regionName(region_name: str, db: Session = Depends(get_db)):
    result = services.get_boundary_by_region(db, region_name)
    if not result:
        raise HTTPException(status_code=404, detail="Boundary not found")
    return JSONResponse(content=jsonable_encoder(result))