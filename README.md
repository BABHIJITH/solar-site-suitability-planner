🌞 Solar Site Suitability Planner
The Solar Site Suitability Planner is a Python-based tool that automates the evaluation of land areas for solar energy development by combining terrain data from Digital Elevation Models (DEM) and solar irradiance estimates from NASA POWER datasets. It uses interpretable, rule-based scoring or machine learning (XGBoost) models to produce a geospatial suitability map, aiding planners, researchers, and enthusiasts in identifying optimal solar farm sites.

🌐 Project Highlights
Geospatial Terrain Analysis using DEMs to assess slope and topography.

Solar Irradiance Data ingestion from NASA POWER APIs for climatic suitability.

Flexible Scoring Methods:

Rule-based scoring for transparent, explainable decisions.

ML-powered suitability prediction using XGBoost for data-driven insights.

Interactive Visualization: Generates an interactive color-coded suitability map using Folium, viewable in web browsers.

Modular, Extensible Codebase: Easily customize with additional features, datasets, or modeling approaches.

Open Source and Beginner-Friendly: Well-structured code to empower learners and professionals alike.

🎯 Features
Feature	Description
Terrain Slope Analysis	Calculates terrain slope from DEM to assess build feasibility.
Solar Irradiance Modeling	Captures spatial solar radiation variations using NASA data or synthetic gradients.
Machine Learning Integration	Uses XGBoost classifiers trained on geospatial features for refined suitability scoring.
Rule-Based Scoring Fallback	Provides stable and transparent scoring without training data.
Interactive Map Output	Generates an HTML map with intuitive color codes (Green: suitable, Orange: moderate, Red: unsuitable).
Large Dataset Handling	Efficiently handles large DEM rasters with optimized visualization subsampling.

📁 Project Structure
text
solar-site-suitability-planner/
├── data/                   # DEM files, downloaded datasets, generated maps
├── models/                 # Persisted machine learning models
├── src/
│   ├── core/
│   │   ├── geodata.py      # Data fetching and validation
│   │   ├── features.py     # Feature extraction (slope, solar irradiance)
│   │   └── scoring.py      # Scoring models (rule-based & ML)
│   └── app/
│       └── dashboard.py   # Interactive map generation
├── requirements.txt        # Python dependencies list
├── main.py                 # Main execution script
└── README.md               # Project documentation

🛠️ Installation and Setup
Prerequisites
Python 3.8 or later (Python 3.11 recommended)

Anaconda or Python with pip

Git LFS for managing large data files like DEM (recommended)

Step-by-Step
Clone the repository

bash
git clone https://github.com/YOUR_USERNAME/solar-site-suitability-planner.git
cd solar-site-suitability-planner
Create and activate a virtual environment

bash
conda create -n solarplanner python=3.11
conda activate solarplanner
Install core geospatial dependencies with conda (important for rasterio and GDAL)

bash
conda install -c conda-forge rasterio gdal
Install remaining Python dependencies

bash
pip install -r requirements.txt
Download or place your DEM file

Download DEM from CGIAR SRTM or USGS EarthExplorer.

Save and rename DEM file as data/dem.tif

Run the main workflow

bash
python main.py
Open the output map

Open data/suitability_map.html in a modern browser to explore site suitability.

🧑‍💻 Usage
The default geographic bounding box is set in main.py (currently Karnataka, India). Change the coordinates there for your region.

Switch between rule-based scoring and ML-based scoring by updating main.py (comment/uncomment relevant code blocks).

Customize subsampling levels in dashboard.py to balance map detail and performance.

Extend feature extraction and model training with additional datasets or machine learning algorithms.

🚀 Next Steps and Enhancements
Integration of more geospatial layers: land use, grid proximity, vegetation indices.

Deployment as a Streamlit or Dash web application for interactive user inputs.

Adding economic feasibility metrics and policy overlays.

Continuous learning with real-world solar farm data.

Export options to GIS formats for further external analysis.

📚 References & Resources
NASA POWER Project

CGIAR SRTM DEM Data

XGBoost Documentation

Folium Python Tutorial


📬 Contact
For questions, feature requests, or contributions, please open an issue or pull request on GitHub, or contact:

Your Name — [abhijithboddu@gmail.com]
GitHub: https://github.com/BABHIJITH

Thank you for exploring sustainable energy solutions with this project!