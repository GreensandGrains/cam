from flask import Flask
import threading
import requests
import time
import os

app = Flask(__name__)

def run_bot():
    # Your existing bot code here
    while True:
        # Replace with your bot's functionality
        print("Bot is running...")
        time.sleep(10)

@app.route('/')
def home():
    return "Bot is running!"

if __name__ == '__main__':
    threading.Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=10000)

# Wait 5 seconds before starting
time.sleep(5)

# Read messages from file
with open("spam.txt", "r", encoding="utf-8") as file:
    messages = file.readlines()

# Get token and channel ID from environment variables
TOKEN = os.getenv("DISCORD_TOKEN2")
CHANNEL_ID = os.getenv("DISCORD_CHANNEL_ID2")

# Safety check
if not TOKEN or not CHANNEL_ID:
    raise Exception("Missing environment variables: DISCORD_TOKEN or DISCORD_CHANNEL_ID")

headers = {
    'authorization': TOKEN,
    'Content-Type': 'application/json'
}

i = 0
while True:
    message = messages[i % len(messages)].strip()
    payload = {'content': message}

    url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"
    r = requests.post(url, json=payload, headers=headers)

    i += 1
    time.sleep(1)  # delay to avoid spam detection
