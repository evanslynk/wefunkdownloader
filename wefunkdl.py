import requests
import sys
import shutil

def download_show(show_number):
    base_url = f"https://www.wefunkradio.com/mirror/stream/{show_number}"
    
    try:
        # Follow the redirect to the actual MP3 file URL
        response = requests.get(base_url, allow_redirects=True)
        response.raise_for_status()
        
        # Get the redirected URL
        mp3_url = response.url
        print(f"Downloading from: {mp3_url}")
        
        # Extract the filename from the URL
        filename = mp3_url.split("/")[-1].split("?")[0]
        
        # Download and save the file
        with requests.get(mp3_url, stream=True) as r:
            r.raise_for_status()
            with open(filename, "wb") as file:
                shutil.copyfileobj(r.raw, file)
        
        print(f"Downloaded show {show_number} as {filename}")
    except requests.RequestException as e:
        print(f"Failed to download show {show_number}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wefunk_dl.py <show_number>")
        sys.exit(1)
    
    show_number = sys.argv[1]
    download_show(show_number)
