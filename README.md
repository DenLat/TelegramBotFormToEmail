# Telegram Bot Form

This project is a Telegram bot that collects form submissions and sends them to an email address.

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd telegram_bot_project
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate  # For Windows
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the bot:**
   - Fill in `config.py` with your details.

5. **Run the bot:**
   ```bash
   python bot.py
   ```

## Configuration

The `config.py` file should contain the following information:

- BOT_TOKEN = 'your_bot_token'
- EMAIL_USER = 'your_email@gmail.com'
- EMAIL_PASSWORD = 'your_password'
- EMAIL_RECEIVER = 'receiver_email@gmail.com'

## Usage

- Start the bot by sending the `/start` command.
- Send your form submission as a message to the bot.
- The bot will send the form submission to the configured email address.

## License

This project is licensed under the MIT License.