# System Information Collector
# This script collects basic system information and saves it to a text file

import socket  # Get computer name and local IP address
import platform  # Get operating system details
import datetime  # Get current date and time
import os  # Get file path information
import getpass  # Get current logged-in username

def get_system_info():
    # Create an empty dictionary to store all system information
    info = {}
    
    # Basic system information
    info['Computer Name'] = socket.gethostname()  # Returns computer's network name
    info['Username'] = getpass.getuser()  # Returns current logged-in user
    
    # Operating system information
    info['OS'] = platform.system()  # Returns OS name (Windows, Linux, Darwin)
    info['OS Version'] = platform.version()  # Returns OS version number
    info['OS Release'] = platform.release()  # Returns OS release identifier
    info['Architecture'] = platform.machine()  # Returns system architecture (x86_64, ARM)
    info['Processor'] = platform.processor()  # Returns processor type/model
    
    # Network information
    info['Local IP'] = socket.gethostbyname(socket.gethostname())  # Converts computer name to IP address
    
    # Timestamp
    info['Date and Time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current time formatted
    
    return info  # Return the complete dictionary

def save_to_file(info):
    # Generate unique filename using current timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"SystemInfo_{timestamp}.txt"  # Example: SystemInfo_20250516_143022.txt
    
    # Open file for writing with UTF-8 encoding
    with open(filename, 'w', encoding='utf-8') as f:
        # Write header
        f.write("=" * 50 + "\n")  # Decorative line (50 equal signs)
        f.write("SYSTEM INFORMATION REPORT\n")  # Report title
        f.write("=" * 50 + "\n\n")  # Decorative line with spacing
        
        # Write each key-value pair from the dictionary
        for key, value in info.items():
            f.write(f"{key}: {value}\n")  # Example: "Computer Name: DESKTOP-ABC123"
        
        # Write footer
        f.write("\n" + "=" * 50 + "\n")  # Decorative line at bottom
        f.write(f"Report generated: {info['Date and Time']}\n")  # Report generation timestamp
    
    return filename  # Return filename so we can show it to user

def main():
    # This is where execution starts
    print("Collecting system information...")  # User feedback
    
    # Call function to gather all information
    info = get_system_info()
    
    # Call function to save information to file
    filename = save_to_file(info)
    
    # Display the absolute path of the saved file
    print(f"Information saved to: {os.path.abspath(filename)}")

# This condition ensures main() runs only when script is executed directly
# (not when imported as a module by another script)
if __name__ == "__main__":
    main()

# WHAT THIS SCRIPT DOES:
# 1. Collects system information (computer name, username, OS, IP, processor, etc.)
# 2. Creates a text file with a unique name using current timestamp
# 3. Saves all information in a formatted, readable way
# 4. Shows the full path where the file was saved

# USE CASES:
# - System inventory documentation
# - Troubleshooting - save system state before making changes
# - Learning Python basics (dictionaries, file I/O, system modules)
# - Creating system snapshots at different times
