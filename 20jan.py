

import os
import shutil
#create a new directory
if not os.path.isdir("test_directory"):
    os.mkdir("test_directory")
#change the current working directory to the nwe directory
os.chdir("test_directory")
print("Current working directory:", os.getcwd())
#create a text file in the directory
with open("example.txt", "w") as file:
    file.write("This is a test file.")
# list files in the current directory
print("files in directory:", os.listdir())
#copy the file
shutil.copy("example.txt", "copy_example.txt")
# Move the copied file to a new location (remaining it in process)
shutil.move("copy_example.txt", "../moved_example.txt")
# go back to the parent directory
os.chdir("..")
# Remove the test directory and its contents
shutil.rmtree("test_directory")
os.remove("moved_example.txt")   #remove the moved files
print("Cleanup Completed!")