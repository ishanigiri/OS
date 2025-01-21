# Monitoring System Resource Usage
# Task: Monitor system resource usage (e.g., CPU and memory stats) by running appropriate system commands 
# such as "top", "ps", or "tasklist", depending on the operating system.
# Learning Goals:
# - Use subprocess.run() to execute system commands.
# - Capture command output using capture_output=True.
# - Write the captured output to a text file for further analysis.

import subprocess
import os

# Step 1: Define the system command based on the operating system
if os.name == "posix":  # For Linux/Mac systems
    command = ["top", "-b", "-n", "1"]  # "top" in batch mode for a single iteration
elif os.name == "nt":  # For Windows systems
    command = ["tasklist"]
else:
    raise OSError("Unsupported operating system.")

# Step 2: Run the system command and capture the output
try:
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Step 3: Check if the command executed successfully
    if result.returncode == 0:
        print("System Resource Usage:")
        print(result.stdout)  # Print the output to the console
        
        # Step 4: Write the output to a text file
        output_file = "system_resource_usage.txt"
        with open(output_file, "w") as f:
            f.write(result.stdout)
        print(f"Output has been written to {output_file}")
    else:
        print("Failed to execute the command.")
        print("Error:", result.stderr)  # Print the error message if the command fails
except Exception as e:
    print(f"An error occurred: {e}")
