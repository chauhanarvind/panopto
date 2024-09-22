import platform
import os

# Function to get the system's default Downloads folder
def get_downloads_folder():
    if platform.system() == "Windows":
        return os.path.join(os.environ['USERPROFILE'], 'Downloads')
    else:
        return os.path.join(os.path.expanduser('~'), 'Downloads')
    
def checkFileExists(save_path, output_file):
     # Ensure the save_path exists, if not create it
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Combine save_path and output_file to get the full output file path
    full_output_path = os.path.join(save_path, output_file)

    # Check if the output file exists and append numbers to the name if necessary
    base, ext = os.path.splitext(full_output_path)  # Split the base name and extension
    counter = 1
    new_output_path = full_output_path

    # Loop to find a unique file name
    while os.path.exists(new_output_path):
        new_output_path = f"{base}_{counter}{ext}"
        counter += 1
    
    return new_output_path