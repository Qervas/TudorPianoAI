import os
import zipfile

# Define the download URL and target directory
download_url = "https://storage.googleapis.com/magentadata/datasets/maestro/v3.0.0/maestro-v3.0.0-midi.zip"
target_dir = "maestro"

# Check if the target directory exists, create it if not
if not os.path.exists(target_dir):
    os.makedirs(target_dir)
    print(f"Created directory: {target_dir}")

# Download the file using a reliable method (consider using libraries like requests or wget)
try:
    # Download logic here (replace with your preferred method)
    # Example using requests (install with `pip install requests`):
    import requests
    response = requests.get(download_url, stream=True)
    with open(os.path.join(target_dir, os.path.basename(download_url)), 'wb') as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)
    # Print download success message
    print(f"Downloaded {download_url} to {target_dir}")
except Exception as e:
    print(f"Error downloading file: {e}")
    exit(1)

# Extract the downloaded zip file
try:
    with zipfile.ZipFile(os.path.join(target_dir, os.path.basename(download_url)), 'r') as zip_ref:
        zip_ref.extractall(target_dir)
    print(f"Extracted maestro-v3.0.0-midi.zip to {target_dir}")
except zipfile.BadZipFile as e:
    print(f"Error extracting zip file: {e}")
    exit(1)

print("Download and extraction completed successfully!")

import shutil

def find_and_copy_midi_files(source_dir, target_dir):
    # Ensure the target directory exists
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Walk through all directories and files in the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.midi'):
                # Construct the full file path
                file_path = os.path.join(root, file)
                # Copy the .midi file to the target directory
                shutil.copy(file_path, target_dir)
                print(f"Copied: {file_path} to {target_dir}")

# Define the source and target directories
source_directory = './maestro/' # Current directory
target_directory = './assets/midi' # Target directory for .midi files

# Call the function to start the process
find_and_copy_midi_files(source_directory, target_directory)

#remove the maestro directory
shutil.rmtree('maestro')

print("All .midi files copied successfully! You can now use them in your project.")