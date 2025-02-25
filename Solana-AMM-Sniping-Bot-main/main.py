import json
import telebot
from telebot import TeleBot
from solders.rpc import RpcClient

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

rpc_endpoint = config['rpc_endpoint']
solana_client = RpcClient(rpc_endpoint)

telegram_token = config['telegram_bot_token']
telegram_chat_id = config['telegram_chat_id']
telegram_bot = TeleBot(telegram_token)

if __name__ == "__main__":
    print("Starting PumpTrader Bot...")
    telegram_bot.polling()
