import os
import subprocess

# Creative Project: System Diagnostics Report
# Task: Write a program that generates a system diagnostics report. The report should include:
# - Current working directory.
# - Disk usage of the current directory.
# - System information (e.g., OS version, processor, memory).
# - Save the report to a text file.

# Learning Goals:
# - Use os to gather filesystem information.
# - Use subprocess to execute system commands (e.g., df for disk usage or uname for OS details).
# - Format and save the results into a text file.

def get_current_working_directory():
    """Get the current working directory."""
    return os.getcwd()

def get_disk_usage(directory):
    """Get disk usage information using the 'df' command."""
    try:
        result = subprocess.check_output(['df', '-h', directory], text=True)
        return result
    except Exception as e:
        return f"Error retrieving disk usage: {e}"

def get_system_information():
    """Get system information using the 'uname' command."""
    try:
        uname_result = subprocess.check_output(['uname', '-a'], text=True)
        return uname_result
    except Exception as e:
        return f"Error retrieving system information: {e}"

def save_report_to_file(report, file_name="system_diagnostics_report.txt"):
    """Save the report to a text file."""
    try:
        with open(file_name, 'w') as file:
            file.write(report)
        print(f"Report saved to {file_name}")
    except Exception as e:
        print(f"Error saving the report: {e}")

def generate_system_diagnostics_report():
    """Generate a system diagnostics report."""
    # Get current working directory
    cwd = get_current_working_directory()

    # Get disk usage of the current directory
    disk_usage = get_disk_usage(cwd)

    # Get system information
    system_info = get_system_information()

    # Format the report
    report = f"""
    System Diagnostics Report
    --------------------------
    Current Working Directory:
    {cwd}

    Disk Usage:
    {disk_usage}

    System Information:
    {system_info}
    """

    # Save the report to a file
    save_report_to_file(report)

# Main program
if __name__ == "__main__":
    generate_system_diagnostics_report()
