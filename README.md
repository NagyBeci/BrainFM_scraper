```markdown
# Brain.fm Track Scraper

This scraper logs into Brain.fm using your credentials, retrieves a streaming token for a specified station, and downloads multiple audio tracks directly to your computer. It helps you quickly obtain music tracks without manual intervention, ensuring no duplicate downloads and organizing files with clear naming conventions.

## Features
- **Automated Login:** Authenticates using your Brain.fm credentials.
- **Token Retrieval:** Fetches a streaming token for a given station ID.
- **Bulk Downloading:** Allows you to specify how many tracks to download at once.
- **No Duplicates:** Skips any track URLs already downloaded.
- **Organized Files:** Saves tracks as `brainfm_station_{station_id}_track_{i}.mp3` for easy identification.
- **Configurable Directory:** Choose the output folder where files are stored.

## Requirements
- **Python 3.x**
- **Libraries:**
  - `requests` for HTTP requests
  - `fake-useragent` to generate user-agent strings
  - `fake-headers` to create realistic HTTP headers
  - `brainfm` for interacting with the Brain.fm API

## Installation
1. **Install Python 3.x** if not already installed.  
   Download from [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Install Required Packages:**
   ```bash
   pip install requests fake-useragent fake-headers brainfm
   ```

3. **Set Your Credentials:**
   Instead of placing your credentials directly in the script, export them as environment variables:
   ```bash
   export BRAINFM_EMAIL="your_email@example.com"
   export BRAINFM_PASSWORD="your_password"
   ```

4. **Configure Script Variables:**
   Open the script in a text editor and change the following values as needed:
   - `station_id` (e.g. `302`): Choose which station to download from.
   - `track_count` (e.g. `20`): How many tracks you’d like to download.
   - `output_dir` (e.g. `./brainfm_downloads`): The folder where files will be saved.

## Usage
1. **Run the Script:**
   ```bash
   python3 download_brainfm_tracks.py
   ```
   
2. **Check the Output:**
   After the script runs, you’ll find MP3 files in your specified output directory, named like:
   ```
   brainfm_station_302_track_0.mp3
   brainfm_station_302_track_1.mp3
   ...
   ```

## Notes
- Make sure your Brain.fm account is active and permitted to access the chosen station.
- Review Brain.fm’s terms of service to ensure that your usage aligns with their policies.
- You can adjust the code for your personal workflow or integrate it into other projects.

## License
This project is provided as-is without warranty. Use at your own risk, and ensure compliance with any relevant terms and conditions.
```
