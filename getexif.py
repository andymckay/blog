import json
import os
import subprocess
import time

#UPDATE = True # Update all the things.
UPDATE = False # Only get new things.

def get_exif():
    start = time.time()
    if os.path.exists("exif.json"):
        with open("exif.json", "r", encoding="utf8") as f:
            exifdata = json.load(f)
    else:
        exifdata = {}
    
    exifdata = update_exif(exifdata)
    end = time.time() - start
    print("✅ Exif fetch complete in {0:.2f} seconds.".format(end))
    return exifdata

def update_exif(exifdata):
    directory = os.path.join(os.getcwd(), "docs/files")

    for file in os.listdir(directory):
        full = os.path.join(directory, file)
        key = "/files/" + file
        if key in exifdata and not UPDATE:
            continue

        if full.lower().endswith((".jpg", ".jpeg")):
            result = subprocess.run(["exiftool", "-j", full], capture_output=1, check=True)
            tags = json.loads(result.stdout)[0]
            exifdata[key] = {
                "lens": tags.get('Lens', tags.get('LensModel', 'Not recorded')),
                "model": tags.get('Model'),
                "iso": tags.get('ISO', tags.get('ISOSpeed', 'Not recorded')),
                "aperture": tags.get('Aperture'),
                "shutter": tags.get('ShutterSpeed'),
                "description": exifdata.get(key, {}).get("description", ""),
            }
            print("✅ Updated:", key)

    with open("exif.json", "w", encoding="utf8") as f:
        json.dump(exifdata, f, indent=2)

    return exifdata

if __name__=='__main__':
    get_exif()
