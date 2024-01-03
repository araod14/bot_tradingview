import telebot
from tradingview_ta import TA_Handler,Interval
import time

import config

#Lists of criptos
symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT", "ADAUSDT", "SOLUSDT", "TRXUSDT", "LINKUSDT", "UNIUSDT"]

# Set up the telegram bot
bot = telebot.TeleBot(config.token)

# Define the function
def retrieve_recomendation_and_price():
    # Retrieve the trading view recomendation
    for symbol in symbols:
        analisis = TA_Handler(
            symbol=symbol,
            screener="crypto",
            exchange="BINANCE",
            interval=Interval.INTERVAL_4_HOURS,
                )

        # Send a message to the user with the recomendation
        # Get the recommendation and price
        recommendation = analisis.get_analysis().summary

        # Send the message
        message = f"{symbol}: {recommendation} ({symbol})"
        bot.send_message(config.chat_id, text=message)

        # Wait for 1 second to avoid hitting the API too frequently
        time.sleep(1)


# Set up the timer to run the function every 5 minutes
while True:
    retrieve_recomendation_and_price()

