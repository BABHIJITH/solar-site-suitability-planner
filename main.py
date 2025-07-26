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

    # --- Rule-based scoring (active) ---
    print("Computing suitability scores with rule-based method...")
    score_grid = scoring.simple_score(feature_array)


    # --- ML-based scoring (commented out) ---
    # print("Extracting flat features for ML...")
    # df, grid_shape = features.extract_flat_features(dem_path, solar_json_path)
    #
    # slope, solar = df.slope.values, df.solar.values
    #
    # # Create labels for supervised training (adjust thresholds as needed)
    # label = ((slope < 15) & (solar > np.percentile(solar, 30))).astype(int)
    # print(f"Label counts: 0={np.sum(label == 0)}, 1={np.sum(label == 1)}")
    #
    # X = df[['slope', 'solar']].values
    # y = label
    #
    # print("Training XGBoost model...")
    # model = scoring.train_xgboost(X, y)
    #
    # print("Predicting suitability with XGBoost model...")
    # score_grid = scoring.predict_suitability_xgb(model, X, grid_shape)

    if not os.path.exists('data'):
        os.makedirs('data')

    print("Plotting results...")
    dashboard.plot_suitability_map(score_grid, dem_path)


if __name__ == '__main__':
    main()
