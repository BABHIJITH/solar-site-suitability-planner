import rasterio
import numpy as np
import pandas as pd

def calculate_slope(dem_path):
    with rasterio.open(dem_path) as src:
        elevation = src.read(1)
        x, y = np.gradient(elevation)
        slope = np.sqrt(x**2 + y**2)
    return slope

def extract_features(dem_path, solar_json_path=None):
    """
    Extract features with synthetic spatial solar irradiance gradient.
    """
    slope = calculate_slope(dem_path)
    if solar_json_path:
        rows, cols = slope.shape
        # Simulate spatial solar irradiance increasing west to east
        solar_array = np.tile(np.linspace(200, 300, cols), (rows, 1))
    else:
        print("Solar data not provided; using zeros.")
        solar_array = np.zeros_like(slope)
    features = np.stack([slope, solar_array], axis=-1)
    return features

def extract_flat_features(dem_path, solar_json_path=None):
    """
    Return flattened feature DataFrame for ML training:
    columns: row, col, slope, solar
    """
    slope = calculate_slope(dem_path)
    if solar_json_path:
        rows, cols = slope.shape
        solar_array = np.tile(np.linspace(200, 300, cols), (rows, 1))
    else:
        solar_array = np.zeros_like(slope)

    records = []
    for r in range(slope.shape[0]):
        for c in range(slope.shape[1]):
            records.append({'row': r, 'col': c, 'slope': slope[r, c], 'solar': solar_array[r, c]})

    return pd.DataFrame(records), slope.shape
