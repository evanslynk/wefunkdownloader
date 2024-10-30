import requests
import sys
import shutil
import subprocess
import os

def download_show(show_number):
    base_url = f"https://www.wefunkradio.com/mirror/stream/{show_number}"
    
    try:
        # Follow the redirect to get the actual MP3 file URL
        response = requests.get(base_url, allow_redirects=True)
        response.raise_for_status()
        
        # Extract the redirected filename with date from the final URL
        mp3_url = response.url
        original_filename = mp3_url.split("/")[-1].split("?")[0]
        compressed_filename = f"compressed_{original_filename}"
        
        # Check if the compressed file already exists
        if os.path.isfile(compressed_filename):
            print(f"{compressed_filename} already exists. Skipping download and encoding.")
            return
        
        # Download the MP3 file only if it does not already exist
        if not os.path.isfile(original_filename):
            print(f"Downloading from: {mp3_url}")
            with requests.get(mp3_url, stream=True) as r:
                r.raise_for_status()
                with open(original_filename, "wb") as file:
                    shutil.copyfileobj(r.raw, file)
            
            print(f"Downloaded show {show_number} as {original_filename}")
        else:
            print(f"{original_filename} already downloaded. Skipping download.")

        # Encode the MP3 to VBR -V6 using ffmpeg
        ffmpeg_command = [
            "ffmpeg", "-i", original_filename, "-codec:a", "libmp3lame", "-qscale:a", "6", compressed_filename
        ]
        subprocess.run(ffmpeg_command, check=True)
        print(f"Encoded to VBR -V6 as {compressed_filename}")
        
        # Delete the original file
        os.remove(original_filename)
        print(f"Deleted the original file: {original_filename}")
        
    except requests.RequestException as e:
        print(f"Failed to download show {show_number}: {e}")
    except subprocess.CalledProcessError as e:
        print(f"ffmpeg encoding failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wefunk_dl.py <show_number>")
        sys.exit(1)
    
    show_number = sys.argv[1]
    download_show(show_number)
