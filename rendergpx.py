import gpxo
import os
from pathlib import Path

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

if __name__ == "__main__":
    p = Path("/Users/a/c/blog/docs/files/gpx/")
    files = list(p.glob("**/*.gpx"))
    print(f"Found {len(files)} GPX files to process.")
    for file in files:
        generate_map(file)