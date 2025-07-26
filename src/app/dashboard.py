import folium
import rasterio

def plot_suitability_map(score_array, dem_path, output_html='data/suitability_map.html'):
    with rasterio.open(dem_path) as src:
        bounds = src.bounds
        transform = src.transform
    center_lat = (bounds.top + bounds.bottom) / 2
    center_lon = (bounds.left + bounds.right) / 2
    m = folium.Map(location=[center_lat, center_lon], zoom_start=8)
    rows, cols = score_array.shape
    step = 20  # plot every 20th cell for performance
    for row in range(0, rows, step):
        for col in range(0, cols, step):
            score = score_array[row, col]
            lon, lat = transform * (col, row)
            color = 'green' if score > 0.7 else 'orange' if score > 0.4 else 'red'
            folium.CircleMarker(
                location=[lat, lon],
                radius=3,
                fill=True,
                fill_opacity=0.6,
                color=color,
                popup=f"Score: {score:.2f}"
            ).add_to(m)
    m.save(output_html)
    print(f"Saved interactive suitability map to {output_html}")
    return m
