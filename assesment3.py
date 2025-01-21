# Fun Challenge: File Cleanup Bot
# Task: Build a program that:
# - Scans a directory for files older than a specified number of days.
# - Moves these files to an "Archive" folder.
# - Deletes the "Archive" folder after confirming with the user.

import os
import shutil
from datetime import datetime, timedelta

# Function to scan directory and move old files to an Archive folder
def cleanup_files(directory, days_old):
    # Create Archive folder if it doesn't exist
    archive_folder = os.path.join(directory, "Archive")
    if not os.path.exists(archive_folder):
        os.makedirs(archive_folder)
    
    # Calculate the cutoff date
    cutoff_date = datetime.now() - timedelta(days=days_old)

    # Loop through the files in the directory
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        # Skip if it's the Archive folder or not a file
        if file_name == "Archive" or not os.path.isfile(file_path):
            continue

        # Get the modification time of the file
        file_mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))

        # Check if the file is older than the specified number of days
        if file_mod_time < cutoff_date:
            print(f"Moving file: {file_name}")
            shutil.move(file_path, os.path.join(archive_folder, file_name))
    
    print("File cleanup completed. Old files moved to 'Archive'.")

# Function to delete the Archive folder after confirmation
def delete_archive_folder(directory):
    archive_folder = os.path.join(directory, "Archive")
    if os.path.exists(archive_folder):
        # Ask for user confirmation
        user_input = input("Do you want to delete the 'Archive' folder? (yes/no): ").strip().lower()
        if user_input == "yes":
            shutil.rmtree(archive_folder)
            print("'Archive' folder deleted.")
        else:
            print("'Archive' folder was not deleted.")
    else:
        print("No 'Archive' folder found.")

# Main program
if __name__ == "__main__":
    # Ask the user for directory path and days
    directory = input("Enter the directory path to scan: ").strip()
    days_old = int(input("Enter the number of days to check for old files: ").strip())

    # Run the cleanup and deletion process
    cleanup_files(directory, days_old)
    delete_archive_folder(directory)
