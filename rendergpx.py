import datetime
import os
import json
from pathlib import Path

import gpxo
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

UPDATE_ALL = True

def generate_map(file):
    parent = file.parent
    gpx = os.path.join(parent, "route.gpx")

    output = os.path.join(parent, "route.html")
    if os.path.exists(output):
        if not UPDATE_ALL:
            print(f"  ⏭️ Skipping existing map image at {output}")
            return
    
    track = gpxo.Track(gpx)
    map = track.folium_map(color='red', tiles='OpenTopoMap', zoom_start=11)
    with open(output, 'w') as f:
        f.write(map._repr_html_())

    print(f"  ✅ Generated map at {output}")

def generate_elevation_plot(file):
    parent = file.parent
    elevation_plot_path = os.path.join(parent, "elevation.png")
    if os.path.exists(elevation_plot_path):
        if not UPDATE_ALL:
            print(f"  ⏭️ Skipping existing elevation plot at {elevation_plot_path}")
            return
    
    gdf = gpd.read_file(file, layer="track_points")
    gdf = gdf[['track_fid','ele', 'time', 'geometry']]
    gdf['time'] = pd.to_datetime(gdf['time'])
    #gdf = gdf.set_index('time')
    plt.style.use('ggplot')
    fig, ax = plt.subplots(1, 1)
    fig.set_size_inches(6, 2)

    # We show a subset of track for the summit in a blue line
    max_height = 0
    min_height = 100000
    elevation_gain = 0
    elevation_loss = 0
    previous_height = None
    max_height = max(elem for elem in gdf['ele'])
    min_height = min(elem for elem in gdf['ele'])
    start = min(elem for elem in gdf['time'])
    elapsed_times = []
    for elem in gdf['time']:
        seconds = (pd.to_datetime(elem) - start).total_seconds()
        elapsed_times.append(str(datetime.timedelta(seconds=seconds)))

    #print(elapsed_times)
    gdf = gdf.assign(elapsed_times=elapsed_times)
    gdf = gdf.set_index('elapsed_times')

    for height in gdf['ele']:
        if previous_height:
            if height > previous_height:
                elevation_gain += height - previous_height
            else:
                elevation_loss += previous_height - height
        
        previous_height = height

    activity_json_path = os.path.join(parent, "activity.json")
    with open(activity_json_path, 'r') as f:
        stats = json.load(f)
        stats.update({
            "max_height": max_height,
            "min_height": min_height,
            "elevation_gain": elevation_gain,
            "elevation_loss": elevation_loss
        })
    
    with open(activity_json_path, 'w') as f:
        json.dump(stats, f, indent=4)
    
    print(f"  ✅ Updated elevation stats at {elevation_plot_path}")
    gdf['ele'].plot(kind='line', ax=ax, color='#2b8cbe')
    # The full track is shown with a grey fill
    ax.fill_between(gdf.index, gdf['ele'].values, color='grey', alpha=0.3)
    plt.tight_layout()
    plt.xlabel(None)

    ax.set_ylim([max(0, min_height - 100), max_height + 10])
    fig.savefig(elevation_plot_path, dpi=300)
    print(f"  ✅ Generated elevation plot at {elevation_plot_path}")

if __name__ == "__main__":
    p = Path("/Users/a/c/blog/docs/files/gpx/")
    files = list(p.glob("**/*.gpx"))
    print(f"Found {len(files)} GPX files to process.")
    for file in files:
        generate_map(file)