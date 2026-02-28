import requests
import json
import sys

url_upload_finalScore = "http://127.0.0.1:8000/geojson/upload_finalscore"
data_path = "data_score/mcdm_score_dolnoslaskie.geojson"

try:
    # 1. Load the file
    with open(data_path, "r", encoding="utf-8") as f:
        geojson_content = json.load(f)
    
    print(f"File loaded. Sending {len(geojson_content.get('features', []))} features to the server...")

    # 2. Send the request
    # 'json=' automatically sets Content-Type to application/json
    response = requests.post(url_upload_finalScore, json=geojson_content)

    # 3. Check for success
    if response.status_code == 201 or response.status_code == 200:
        print("✅ Success!")
        print(response.json())
    else:
        print(f"❌ Failed with status code: {response.status_code}")
        print(response.text)

except FileNotFoundError:
    print(f"❌ Error: Could not find file at {data_path}")
except requests.exceptions.ConnectionError:
    print("❌ Error: Could not connect to FastAPI. Is uvicorn running?")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")