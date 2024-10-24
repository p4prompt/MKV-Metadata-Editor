import subprocess
import os
import shutil
import re

def set_mkv_metadata(input_file, output_file):
    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Input file not found: {input_file}")
        return

    # Copy the input file to the output file path
    try:
        print(f"Copying {input_file} to {output_file}...")
        shutil.copyfile(input_file, output_file)
    except Exception as e:
        print(f"Error copying file: {e}")
        return

    # Set the global title
    try:
        print(f"Setting global title to 'My Vid' for {output_file}")
        subprocess.run(['mkvpropedit', output_file, '--edit', 'info', '--set', 'title=My Vid'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error setting global title: {e}")

    # Use mkvinfo to get track details
    try:
        result = subprocess.run(['mkvinfo', input_file], capture_output=True, text=True, check=True)
        mkv_info = result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving MKV info: {e}")
        return

    # Regular expressions to match track information
    track_info_re = re.compile(r"\+ Track number: (\d+) \(track ID for mkvmerge & mkvextract: \d+\).*?\+ Track type: (\w+)", re.DOTALL)

    # Find all track details (track number and type)
    tracks = track_info_re.findall(mkv_info)

    # Go through each track and rename it based on its type
    for track_number, track_type in tracks:
        track_type = track_type.strip()

        # Track numbers start from 1, so we use them directly.
        try:
            if track_type == "video":
                print(f"Setting title for video track {track_number} to 'Google Video'")
                subprocess.run(['mkvpropedit', output_file, '--edit', f"track:{track_number}", '--set', 'name=Google Video'], check=True)
            elif track_type == "audio":
                print(f"Setting title for audio track {track_number} to 'Google Audio'")
                subprocess.run(['mkvpropedit', output_file, '--edit', f"track:{track_number}", '--set', 'name=Google Audio'], check=True)
            elif track_type == "subtitles":
                print(f"Setting title for subtitle track {track_number} to 'Google Subtitle'")
                subprocess.run(['mkvpropedit', output_file, '--edit', f"track:{track_number}", '--set', 'name=Google Subtitle'], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error setting {track_type} track title: {e}")

    print("Done.")

if __name__ == "__main__":
    # Prompt user for input and output file paths
    input_file = input("Enter the path to the input MKV file: ")
    output_file = input("Enter the path to save the modified MKV file: ")

    # Run the metadata update process
    set_mkv_metadata(input_file, output_file)
