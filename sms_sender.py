#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
📱 SMS Sender with Twilio
Send SMS messages using Twilio API
Author: [Your Name]
Version: 1.0.0
"""

import os  # Import OS module for environment variables
from twilio.rest import Client  # Import Twilio REST API client

# ============================================
# CONFIGURATION - Get from https://www.twilio.com/console
# ============================================

ACCOUNT_SID = 'your_account_sid'  # Twilio Account SID - Unique identifier for your account
AUTH_TOKEN = 'your_auth_token'    # Twilio Auth Token - Secret key for authentication
TWILIO_PHONE = '+1234567890'      # Twilio phone number - Must be in international format

# ============================================
# MAIN FUNCTION
# ============================================

def send_sms_twilio(to_numbers, message):
    """
    Send SMS messages to multiple recipients using Twilio
    
    Parameters:
    -----------
    to_numbers : list
        List of recipient phone numbers in international format
        Example: ['+989123456789', '+989876543210']
    
    message : str
        The text message to send (max 1600 characters)
    
    Returns:
    --------
    None - Prints success/failure status for each number
    
    How it works:
    -------------
    1. Creates a Twilio client with your credentials
    2. Iterates through each phone number in the list
    3. Sends the message using Twilio's API
    4. Prints success message with SID (unique message ID)
    5. Prints error message if sending fails
    """
    
    # Create Twilio client instance with account credentials
    # Client handles authentication and API communication
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    
    # Loop through each phone number in the list
    for number in to_numbers:
        try:
            # Send message using Twilio API
            # create() method sends SMS and returns message object
            message = client.messages.create(
                body=message,          # The text content of the SMS
                from_=TWILIO_PHONE,     # Your Twilio phone number (sender)
                to=number               # Recipient phone number
            )
            
            # Print success message with unique message SID
            # message.sid is a unique identifier for tracking the message
            print(f"✅ Message sent to {number}. SID: {message.sid}")
            
        except Exception as e:
            # Catch and display any errors during sending
            # Common errors: invalid number, insufficient balance, auth failure
            print(f"❌ Error sending to {number}: {e}")

# ============================================
# USAGE EXAMPLE
# ============================================

# List of recipient phone numbers in international format
# For Iran: +989xxxxxxxxx (replace x with actual digits)
numbers = ['+989123456789', '+989876543210']

# Send the message
send_sms_twilio(numbers, 'سلام! این یک پیام تست است.')

# ============================================
# ENVIRONMENT VARIABLES (Recommended for production)
# ============================================

"""
To keep credentials secure, use environment variables instead of hardcoding:

1. Set environment variables:
   export TWILIO_ACCOUNT_SID='your_sid'
   export TWILIO_AUTH_TOKEN='your_token'
   export TWILIO_PHONE_NUMBER='+1234567890'

2. Use in code:
   ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
   AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
   TWILIO_PHONE = os.getenv('TWILIO_PHONE_NUMBER')

3. Or use .env file with python-dotenv:
   from dotenv import load_dotenv
   load_dotenv()
"""

# ============================================
# TROUBLESHOOTING
# ============================================

"""
Common errors and solutions:

Error 20003: Authentication failed
    - Check ACCOUNT_SID and AUTH_TOKEN are correct
    - Make sure you're using Live credentials, not Test

Error 21211: Invalid phone number
    - Number must be in international format: +[country code][number]
    - For Iran: +989xxxxxxxxx (remove leading 0)

Error 21614: 'To' number not verified
    - Trial accounts can only send to verified numbers
    - Add and verify numbers in Twilio console

Error 20404: Not enough balance
    - Add funds to your Twilio account
    - Check free trial credit is exhausted

Rate limiting:
    - Free tier: 1 message per second
    - Add delay between messages if sending in bulk
"""

# ============================================
# BULK SENDING WITH DELAY (Optional enhancement)
# ============================================

"""
For sending to many numbers, add a delay to avoid rate limiting:

import time

def send_sms_bulk(to_numbers, message, delay=1):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for i, number in enumerate(to_numbers):
        try:
            msg = client.messages.create(body=message, from_=TWILIO_PHONE, to=number)
            print(f"✅ {i+1}/{len(to_numbers)} Sent to {number}. SID: {msg.sid}")
        except Exception as e:
            print(f"❌ Failed to {number}: {e}")
        time.sleep(delay)  # Wait between messages
"""

# ============================================
# MAIN ENTRY POINT
# ============================================

if __name__ == '__main__':
    # This block runs only when script is executed directly
    # Not when imported as a module
    print("=" * 50)
    print("📱 SMS Sender with Twilio")
    print("=" * 50)
    print("Configuration:")
    print(f"   Account SID: {ACCOUNT_SID[:5]}...{ACCOUNT_SID[-5:]}")
    print(f"   Twilio Phone: {TWILIO_PHONE}")
    print(f"   Recipients: {len(numbers)} numbers")
    print("=" * 50)
    
    # Uncomment to run the example
    # send_sms_twilio(numbers, 'Test message from Twilio!')
