import os
import shutil

# Source and destination directories
source_dir = '/Users/avryjackson/Desktop/TestFolder'       # Replace with your source folder
destination_dir = '/Users/avryjackson/Desktop/psdfolder'  # Replace with your destination folder

# Create destination directory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

# Loop through files in source directory
for filename in os.listdir(source_dir):
    if filename.lower().endswith('.psd'):  # Case-insensitive check for .psd
        src_path = os.path.join(source_dir, filename)
        dest_path = os.path.join(destination_dir, filename)
        
        # Move the file
        shutil.move(src_path, dest_path)
        print(f"Moved: {filename}")
