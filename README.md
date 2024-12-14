# Project Title: Brain.fm Track Downloader

This project provides a Python script to authenticate with Brain.fm, fetch a streaming token, and download audio tracks from a specified Brain.fm station into a designated folder. It also ensures that no duplicate downloads occur, organizes the downloaded files with a clear naming convention, and allows for easy customization of the output directory and the number of tracks to download.

## Features:
- Login to Brain.fm using your credentials.
- Obtain a streaming token for a chosen station.
- Download multiple audio tracks directly to a specified folder.
- Use a clear and descriptive naming scheme for output files (e.g., `brainfm_station_{station_id}_track_{i}.mp3`).
- Prevent duplicate downloads by checking and skipping previously downloaded track URLs.
- Adjust the number of tracks to download and the folder location as needed.

## Requirements:
- Python 3.x
- `requests` library for HTTP requests.
- `fake_useragent` and `fake_headers` libraries to generate plausible user-agent strings and headers.
- `brainfm` Python library (not part of standard Python, you must install it).
- A valid Brain.fm account with credentials (email and password).

## Setup and Installation:
1. Install Python 3.x if not already installed.
2. Install required packages:
