import os
import warnings
import requests
from fake_useragent import UserAgent
from fake_headers import Headers
import brainfm

warnings.filterwarnings("ignore")

def login_to_brainfm(email, password):
    """Login to Brain.fm and return a client connection."""
    ua = UserAgent()
    client = brainfm.Connection(user_agent=ua.ie)
    client.login(email, password)
    return client

def get_token(client, station_id=302):
    """Get a streaming token for the given station from Brain.fm."""
    return client.get_token(station_id)

def download_tracks(client, token, station_id=302, count=20, output_dir=".", prefix="brainfm_station"):
    """
    Download tracks from Brain.fm without duplicates.
    - `client`: Authenticated Brain.fm client
    - `token`: Streaming token for the station
    - `station_id`: ID of the station
    - `count`: Number of tracks to attempt to download
    - `output_dir`: Directory where files will be saved
    - `prefix`: Filename prefix for downloaded files
    """

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    session = requests.Session()
    headers = Headers(os="mac", headers=True).generate()

    downloaded_urls = set()

    for i in range(count):
        if i % 5 == 0:
            print(f"Attempting to download track {i}/{count}...")

        url = client.make_stream_url(token)

        # Check for duplicates before downloading
        if url in downloaded_urls:
            print(f"Skipping duplicate URL: {url}")
            continue

        response = session.get(url, allow_redirects=True, verify=True, headers=headers)

        if response.status_code == 200:
            filename = f"{prefix}_{station_id}_track_{i}.mp3"
            filepath = os.path.join(output_dir, filename)

            with open(filepath, "wb") as f:
                f.write(response.content)

            downloaded_urls.add(url)
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download track {i}. Status code: {response.status_code}")

def main():
    # Replace with your actual credentials or retrieve them from environment variables
    email = os.environ.get("BRAINFM_EMAIL", "your_email@example.com")
    password = os.environ.get("BRAINFM_PASSWORD", "your_password")

    # Configure these variables as needed
    station_id = 302
    track_count = 20
    download_folder = "./brainfm_downloads"  # specify your folder

    client = login_to_brainfm(email, password)
    token = get_token(client, station_id)
    download_tracks(client, token, station_id=station_id, count=track_count, output_dir=download_folder)

if __name__ == "__main__":
    main()
