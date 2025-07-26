import os
from src.core import geodata, features, scoring
from src.app import dashboard

def main():
    area_bbox = [74.0, 11.0, 78.0, 15.0]  # Karnataka example

    print("Downloading or loading datasets...")
    solar_json_path = geodata.download_nasa_power(area_bbox)
    dem_path = geodata.load_dem()
    if dem_path is None:
        print("DEM file missing. Please download DEM and place as data/dem.tif.")
        return

    print("Extracting features...")
    feature_array = features.extract_features(dem_path, solar_json_path)

    print("Computing suitability scores with rule-based method...")
    score_grid = scoring.simple_score(feature_array)

    if not os.path.exists('data'):
        os.makedirs('data')

    print("Plotting results...")
    dashboard.plot_suitability_map(score_grid, dem_path)

if __name__ == '__main__':
    main()
