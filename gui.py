from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image

from tradingview_ta import TA_Handler,Interval
import time


#Lists of criptos
symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT", "ADAUSDT", "SOLUSDT", "TRXUSDT", "LINKUSDT", "UNIUSDT"]


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

        # print the message
        message = f"{recommendation['RECOMMENDATION']}"
        print(message)

        # Wait for 1 second to avoid hitting the API too frequently
        time.sleep(1)


class Registro():
    def __init__(self, ventana):
        self.window = ventana
        self.window.title('Recomendaciones de TradingView')
        self.window.geometry('290x400')
        self.window.resizable(0,0)
        self.window.config(bd=10)

        # -------------- titulo -----------
        titulo = Label(ventana, text='Recomendaciones \npara Compra/Venta', fg="black", font=("Times New Roman", 13, "bold"), pady=5).pack()

        # -------------- Logo nuevo usuario
        imagen_binance = Image.open('./download (2).png')
        nueva_imagen = imagen_binance.resize((40,40))
        render = ImageTk.PhotoImage(nueva_imagen)
        label_imagen = Label(ventana, image=render)
        label_imagen.image = render
        label_imagen.pack(pady=5)

        # -------------- Marco --------------
        marco = LabelFrame(ventana, text='Criptomonedas', font=('Comic Sans', 10, 'bold'))
        marco.config(bd=2, pady=5)
        marco.pack()

        # ------------- Formulario -------------
        btc = Label(marco, text='BTC', font=("Comic Sans", 10,"bold")).grid(row=0, column=0, sticky='s', padx=5, pady=8)
        self.btc_valor = Label(marco, width=25)
        self.btc_valor.focus()
        self.btc_valor.grid(row=0, column=1, padx=5, pady=8)

        eth = Label(marco, text='ETH', font=("Comic Sans", 10,"bold")).grid(row=1, column=0, sticky='s', padx=10, pady=8)
        self.eth_valor = Label(marco, width=25)
        self.eth_valor.grid(row=1, column=1, padx=10, pady=8)

        bnb = Label(marco, text='BNB', font=("Comic Sans", 10,"bold")).grid(row=2, column=0, sticky='s', padx=10, pady=8)
        self.bnb_valor = Label(marco, width=25)
        self.bnb_valor.grid(row=2, column=1, padx=10, pady=8)

        xrp = Label(marco, text='XRP', font=("Comic Sans", 10,"bold")).grid(row=3, column=0, sticky='s', padx=10, pady=8)
        self.xrp_valor = Label(marco, width=25)
        self.xrp_valor.grid(row=3, column=1, padx=10, pady=8)

        ada = Label(marco, text='ADA', font=("Comic Sans", 10,"bold")).grid(row=4, column=0, sticky='s', padx=10, pady=8)
        self.ada_valor = Label(marco, width=25)
        self.ada_valor.grid(row=4, column=1, padx=10, pady=8)

        sol = Label(marco, text='SOL', font=("Comic Sans", 10,"bold")).grid(row=5, column=0, sticky='s', padx=10, pady=8)
        self.sol_valor = Label(marco, width=25)
        self.sol_valor.grid(row=5, column=1, padx=10, pady=8)

        trx = Label(marco, text='TRX', font=("Comic Sans", 10,"bold")).grid(row=6, column=0, sticky='s', padx=10, pady=8)
        self.trx_valor = Label(marco, width=25)
        self.trx_valor.grid(row=6, column=1, padx=10, pady=8)

        link = Label(marco, text='LINK', font=("Comic Sans", 10,"bold")).grid(row=7, column=0, sticky='s', padx=10, pady=8)
        self.link_valor = Label(marco, width=25)
        self.link_valor.grid(row=7, column=1, padx=10, pady=8)

        uni = Label(marco, text='UNI', font=("Comic Sans", 10,"bold")).grid(row=7, column=0, sticky='s', padx=10, pady=8)
        self.uni_valor = Label(marco, width=25)
        self.uni_valor.grid(row=8, column=1, padx=10, pady=8)

if __name__ == '__main__':

    while True:
        print("Bot is running")
        retrieve_recomendation_and_price()
        ventana = Tk()
        application = Registro(ventana)
        ventana.mainloop()

