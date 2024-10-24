# MKV-Metadata-Editor

This Python script allows users to modify the metadata of an MKV (Matroska) file, including changing the global title and renaming tracks (video, audio, subtitles) based on their type. It uses `mkvpropedit` to edit metadata and `mkvinfo` to retrieve track information.

## Features
- Copy an MKV file and update its metadata.
- Set a custom global title for the MKV file.
- Automatically detect video, audio, and subtitle tracks and rename them accordingly:
  - Video tracks are renamed to "Google Video".
  - Audio tracks are renamed to "Google Audio".
  - Subtitle tracks are renamed to "Google Subtitle".

## Prerequisites
- Python 3.x is required.
- MKVToolNix must be installed, as the script uses `mkvpropedit` and `mkvinfo` from this package.

### Installing MKVToolNix
- On Ubuntu/Debian:
  ```bash
  sudo apt-get install mkvtoolnix

- On macOS (using Homebrew):
  ```bash
  brew install mkvtoolnix

## Installation
- Clone this repository:
  ```bash
  https://github.com/p4prompt/MKV-Metadata-Editor/
  
- Install the required dependencies (if any). Currently, this script does not rely on external Python libraries other than built-in modules.


## Usage

Run the script:
  ```bash
  python3 mkv_metadata_editor.py
  ```
Enter the path to your input MKV file and the path where you'd like to save the modified MKV file when prompted.

- Example:
  ```bash
  Enter the path to the input MKV file: /path/to/input.mkv
  Enter the path to save the modified MKV file: /path/to/output.mkv
  ```
The script will:
 - Copy the input MKV to the specified output location.
 - Change the global title to My Vid.
 - Rename the video, audio, and subtitle tracks based on their type.


## Contributions
Feel free to submit issues or pull requests if you have suggestions for improvements.




