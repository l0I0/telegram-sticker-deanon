# Telegram Sticker Deanon

A simple Python script to get the creator's ID of any Telegram sticker pack.

## Features
- Extract sticker pack ID
- Get user ID

## Requirements
- Python 3.7+
- Pyrogram
- TgCrypto

## Installation

1. Clone the repository:
```bash
git clone https://github.com/l0I0/telegram-sticker-deanon.git
cd telegram-sticker-deanon
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Create `config.py` file with your Telegram API credentials:
```python
API_ID = "your_api_id"
API_HASH = "your_api_hash"
```

You can get your API credentials at [my.telegram.org](https://my.telegram.org)

## Usage

1. Run the script:
```bash
python main.py
```

2. Enter the sticker pack URL when prompted:
```bash
Enter sticker pack URL: https://t.me/addstickers/YourStickerPack
```

3. The script will output the sticker pack ID and creator's user ID:
```bash
Sticker pack ID: 123456789
User ID: 987654321
```