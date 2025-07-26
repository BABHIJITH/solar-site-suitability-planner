import requests
import os

def download_nasa_power(area_bbox, out_file='data/solar.json'):
    """
    Download solar irradiance data (clear sky surface shortwave downward radiation) from NASA POWER API.
    area_bbox: [min_lon, min_lat, max_lon, max_lat]
    """
    lon = (area_bbox[0] + area_bbox[2]) / 2
    lat = (area_bbox[1] + area_bbox[3]) / 2
    url = (
        f"https://power.larc.nasa.gov/api/temporal/climatology/point?"
        f"parameters=CLRSKY_SFC_SW_DWN&community=RE"
        f"&longitude={lon}&latitude={lat}"
        f"&format=JSON"
    )
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Save raw JSON for later use or processing
        os.makedirs(os.path.dirname(out_file), exist_ok=True)
        with open(out_file, 'w') as f:
            import json
            json.dump(data, f, indent=2)
        print(f"Downloaded NASA POWER data saved to {out_file}")
        return out_file
    else:
        print("Failed to download NASA POWER data")
        return None

def load_dem(path='data/dem.tif'):
    if os.path.exists(path):
        print(f"DEM file found at {path}")
        return path
    else:
        print(f"DEM file NOT found at {path}. Please download and place it in the data/ folder.")
        return None
