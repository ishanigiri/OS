import subprocess
import os

# run a simple command and capture its output
result = subprocess.run(["echo", "Hello, World!"], capture_output=True, text=True)
print("Command Output:", result.stdout)

#list files in the current directory using "ls" or "dir" (platform-specific)
command = ["ls"] if os.name != "nt" else ["dir"]
result = subprocess.run(command, capture_output=True, text= True, shell=True)
print("Files in the current directory:")
print(result.stdout)
#check for errors (e.g., invalid command)
result = subprocess.run(["fake_command"], capture_output=True, text= True)
if result.returncode !=0:
    print("Error:", result.stderr);
    