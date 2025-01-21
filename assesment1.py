# Task: Write a script that takes a directory path as input and creates a zip file backup of its contents.
# The backup file should be named with the current date and time.
# 
# Learning Goals:
# - Utilize the 'os' module to navigate and identify the directory structure.
# - Leverage the 'shutil' module for creating archives using shutil.make_archive().
# - Use Python’s 'datetime' module to generate timestamped backup filenames.

import os
import shutil
from datetime import datetime

def backup_directory(directory_path):
    # Check if the provided path exists and is a directory
    if not os.path.isdir(directory_path):
        print(f"The path {directory_path} is invalid or not a directory.")
        return

    # Get the current date and time to create a unique backup filename
    current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_filename = f"backup_{current_time}"

    # Create a zip file using shutil.make_archive
    shutil.make_archive(backup_filename, 'zip', directory_path)

    print(f"Backup created successfully: {backup_filename}.zip")

# Example usage
directory_to_backup = input("Enter the directory path to back up: ")
backup_directory(directory_to_backup)
