import os

def load_map(filename):
    # Define the directory where map files are located
    maps_dir = 'maps/'
    # Ensure the maps directory exists
    if not os.path.isdir(maps_dir):
        raise FileNotFoundError(f"The directory '{maps_dir}' does not exist.")
    # Construct the full path to the map file
    file_path = os.path.join(maps_dir, filename)
    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{filename}' does not exist in the '{maps_dir}' directory.")
    # Open and read the map file
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file]
