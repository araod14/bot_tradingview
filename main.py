import telebot
from tradingview_ta import TA_Handler,Interval
import time

#Lists of criptos
symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT", "ADAUSDT", "SOLUSDT", "TRXUSDT", "LINKUSDT", "UNIUSDT"]

# Set up the telegram bot
bot = telebot.TeleBot(token='YOUR_BOT_TOKEN')

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
        message = f"Tradingview recomendation is:{symbol,analisis.get_analysis().summary:.2f} USDT\n"
        bot.send_message(chat_id='YOUR_CHAT_ID', text=message)

# Set up the timer to run the function every 5 minutes
while True:
    retrieve_recomendation_and_price
    time.sleep(300)
