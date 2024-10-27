# Telegram Bot Project

This repository contains a custom Telegram bot that automates certain tasks and commands, built using Python and the `pyTelegramBotAPI`. The bot is designed to execute a DDoS attack and includes user management with MongoDB integration. It is configured to run in a GitHub Codespace, with a `keep_alive.sh` file ensuring the bot runs continuously.

## ⚠️ TO RUN YOUR CODESPACE ⚠️
```bash
./keep_alive.sh & python3 sahil.py
```

## Project Structure

- `sahil.py`: The main Python script that runs the Telegram bot. It manages command handling and attacks. This `sahil.py` executes the encrypted file `sahil.py.enc`. This code is all about TG Bot button operations.
- `bgmi`: An executable file that handles the attack logic. This is the main file.
- `config.json`: Configuration file that holds bot token and admin IDs.
- `keep_alive.sh`: A bash script to ping the Codespace periodically to keep it alive.
- `install.sh`: Shell script that sets up the environment for the bot inside the Codespace.
- `users.txt`: To store allowed users Telegram User ID.
- `developers.txt`: The developer's signature.
- `user_attack_details.json`: This file contain users all TG bot operation logs.
- `decrypted.sahil.py`: This contains the decypted code of `sahil.py.enc` (XOR and BASE64 Encrypted), and the key is inside `sahil.py`.
- `.github/workflows/keep_alive.yml`: GitHub Actions workflow that pings the Codespace every 5 minutes to keep it alive.

## Prerequisites

- Python 3.8+
- MongoDB (not used here)
- GitHub Codespace (or any other remote environment)
- `pyTelegramBotAPI` library

## Setup and Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/yourusername/your-repository.git
cd your-repository
```

### Step 2: Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install pyTelegramBotAPI
```

### Step 3: Configure the Bot

Update the `config.json` file with your bot token and admin IDs.

### Step 4: Run the Bot

To run the bot and keep it alive:

```bash
./keep_alive.sh & python3 sahil.py
```

This command runs the `keep_alive.sh` script in the background and starts the bot.

### Tips:

- Make sure your Codespace URL is correct in the `keep_alive.sh` file.
- Use `python3 sahil.py` to run the bot.
- To stop the bot, kill the running processes by using `ps aux | grep python` and `kill [PID]`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
