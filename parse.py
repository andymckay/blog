import os
import json
import re
import requests
import shutil
from stravalib.client import Client

with open(".strava.json", "r", encoding="utf8") as f:
    token_refresh = json.load(f)



def list_content_files(content_dir='./content'):
    """List all markdown files in the content directory."""
    files = []
    for root, dirs, filenames in os.walk(content_dir):
        for filename in filenames:
            if filename.endswith('.md'):
                filepath = os.path.join(root, filename)
                files.append(filepath)
    return files

def extract_strava_iframes(filepath):
    """Extract Strava activity IDs from a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    activity_ids = []
    # Pattern for iframe URLs
    pattern1 = r"https://www\.strava\.com/activities/(\d+)/embed/"
    activity_ids.extend(re.findall(pattern1, content))
    
    # Pattern for [gpx#ID] format
    pattern2 = r"\[gpx#(\d+)\]"
    activity_ids.extend(re.findall(pattern2, content))
    
    # Pattern for data-embed-id format
    pattern3 = r"data-embed-id='(\d+)'"
    activity_ids.extend(re.findall(pattern3, content))
    
    return activity_ids

def fetch_strava_activity_times(activity_id, client):
    """Fetch elapsed and moving time for a Strava activity."""
    try:
        activity = client.get_activity(activity_id)
        elapsed_time = activity.elapsed_time
        moving_time = activity.moving_time
        distance = activity.distance
        photos = client.get_activity_photos(activity_id)
        return elapsed_time, moving_time, distance, photos
    except Exception as e:
        print(f"  ❌ Error fetching times for activity {activity_id}: {e}")
        raise

def download_photo(url, filepath):
    """Download a photo from URL and save to filepath."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(filepath, 'wb') as f:
            f.write(response.content)
        return True
    except Exception as e:
        print(f"    ❌ Error downloading photo: {e}")
        return False

def find_and_copy_photo(photo_id, source_dir, dest_dir):
    """Find a photo by ID in source directory and copy to destination."""
    try:
        for filename in os.listdir(source_dir):
            if filename.startswith(photo_id) and filename.endswith('.jpg'):
                source_path = os.path.join(source_dir, filename)
                dest_path = os.path.join(dest_dir, filename)
                shutil.copy2(source_path, dest_path)
                return True
        return False
    except Exception as e:
        print(f"    ❌ Error copying photo {photo_id}: {e}")
        return False

def download_gpx(activity_id, dest_dir):
    """Download GPX export for a Strava activity."""
    try:
        url = f"https://www.strava.com/activities/{activity_id}/export_gpx"
        cookies = "_sp_id.047d=e79d5e68-dd8f-4ec4-b929-35a98800d43d.1707009576.143.1768699335.1768342914.54aa14c1-e247-4f43-8bde-e7080ea7f6e4; sp=422c5148-f4f3-4e50-8f0c-ce212a34c20f; _ga_12345=GS2.1.s1768697729$o1$g0$t1768697729$j60$l0$h1775099131; strava_remember_id=5871759; strava_remember_token=eyJzaWduaW5nX2tleSI6InYxIiwiZW5jcnlwdGlvbl9rZXkiOiJ2MSIsIml2IjoiUC9tTXpWNjBsU0M0Q2thS2Z5R2E4UT09XG4iLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjb20uc3RyYXZhLmF0aGxldGVzIiwic3ViIjo1ODcxNzU5LCJpYXQiOjE3NjY3ODE1NTEsImV4cCI6MTc2OTM3MzU1MSwiZW1haWwiOiJqU2R0UEpPUUZpb1VaZmNERGJYQW1XaXZhQXl1cWVCUElOQkRPK3duSytnRUhwcXV5a2tjcnJzTXNBaGFcbmlrbWgzS2w2ZnBZYUFzNnAwOVduWWF3bC9RPT1cbiJ9.dKQdQ1feoeYU72hASvgTVGIP5RoDwrKyI2KklI1A0VI; _strava_cpra=opted_out; CookieConsent={stamp:%27bcNT6B1q2d1Rc6fNV3lO+DZ80/rmyyi+x5RltX3A6ybdHJuMQHx02w==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:false%2Cmethod:%27explicit%27%2Cver:2%2Cutc:1766781554945%2Cregion:%27ca%27}; _strava4_session=mc4cuhrqci7n3k0bjpmtvqf7ute05j1d; _currentH=d3d3LnN0cmF2YS5jb20=; _sp_ses.047d=*; ttcsid_CRCAPDJC77UE5B95LUQG=1768697706782::8B-SgVvuWmQeSw4tliEX.1.1768699334555.1; ttcsid=1768697730910::hEHivmPd4S_14BtxJRL-.1.1768699334555.0"
        headers = {"Cookie": cookies}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        gpx_filepath = os.path.join(dest_dir, 'route.gpx')
        with open(gpx_filepath, 'w', encoding='utf-8') as f:
            f.write(response.text)
        return True
    except Exception as e:
        print(f"    ❌ Error downloading GPX for activity {activity_id}: {e}")
        raise

if __name__ == '__main__':    
    client = Client(
        access_token=token_refresh["access_token"],
        refresh_token=token_refresh["refresh_token"],
        token_expires=token_refresh["expires_at"],
    )
    
    # Create output directory
    output_dir = './docs/files/gpx'
    os.makedirs(output_dir, exist_ok=True)
    
    content_files = list_content_files()
    unique_ids = ["15495517267"]
    print(f"\n\nTotal unique Strava activity IDs found: {len(unique_ids)}")
    
    print("\nFetching activity times...")
    export_media_dir = os.path.expanduser('~/Downloads/export_5871759/media')
    for activity_id in sorted(unique_ids):
        activity_dir = os.path.join(output_dir, str(activity_id))
        
        # Skip if activity directory already exists
        if os.path.exists(activity_dir):
            print(f"  ⏭️ Activity {activity_dir}: already exists, skipping")
            continue
        
        os.makedirs(activity_dir, exist_ok=True)
        elapsed_time, moving_time, distance, photos = fetch_strava_activity_times(activity_id, client)
        if elapsed_time is not None:
            # Download GPX file
            if download_gpx(activity_id, activity_dir):
                print(f"    ✅ Downloaded GPX route")
            
            # Find and copy photos
            photo_list = []
            for idx, photo in enumerate(photos):
                photo_id = photo.unique_id
                photo_list.append(photo_id)
                if find_and_copy_photo(photo_id, export_media_dir, activity_dir):
                    print(f"    ✅ Copied photo {idx + 1}")
                else:
                    print(f"    ⚠️ Photo {idx + 1} not found in export directory")

            activity_data = {
                "activity_id": activity_id,
                "elapsed_time_seconds": elapsed_time,
                "moving_time_seconds": moving_time,
                "distance_meters": distance,
                "photos": photo_list
            }
            
            json_filepath = os.path.join(activity_dir, 'activity.json')
            with open(json_filepath, 'w', encoding='utf-8') as f:
                json.dump(activity_data, f, indent=2)
            
            print(f"  ✅ Activity {activity_id}: {len(photo_list)} photos found")
            print(f"     Saved to: {json_filepath}")