import numpy as np
import xgboost as xgb
import joblib
import os

def train_xgboost(X, y, model_path='models/xgb_model.joblib'):
    model = xgb.XGBClassifier(n_estimators=100, max_depth=4, random_state=42)
    model.fit(X, y)
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    return model

def load_xgboost(model_path='models/xgb_model.joblib'):
    return joblib.load(model_path)

def predict_suitability_xgb(model, X, grid_shape):
    preds = model.predict_proba(X)[:, 1]  # probability of class 1
    grid = preds.reshape(grid_shape)
    return (grid - np.min(grid)) / (np.max(grid) - np.min(grid) + 1e-9)  # normalized 0-1

def simple_score(features):
    slope = features[..., 0]
    solar = features[..., 1]
    max_solar = np.max(solar) if np.max(solar) > 0 else 1
    norm_solar = solar / max_solar
    slope_penalty = np.where(slope > 10, 0.0, 1.0 - (slope / 10))
    score = norm_solar * slope_penalty
    score = (score - np.min(score)) / (np.max(score) - np.min(score) + 1e-9)
    return score
