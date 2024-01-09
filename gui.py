from tkinter import *
from PIL import ImageTk, Image
from tradingview_ta import TA_Handler,Interval


class Registro():
    def __init__(self, ventana):
        self.window = ventana
        self.window.title('Recomendaciones de TradingView')
        self.window.geometry('290x450')
        self.window.resizable(0,0)
        self.window.config(bd=10)

        # -------------- titulo -----------
        titulo = Label(ventana, text='Recomendaciones \npara Compra/Venta', fg="black", font=("Times New Roman", 13, "bold"), pady=5).pack()

        # -------------- Logo nuevo binance
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

        # ------------- Criptos -------------
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

        uni = Label(marco, text='UNI', font=("Comic Sans", 10,"bold")).grid(row=8, column=0, sticky='s', padx=10, pady=8)
        self.uni_valor = Label(marco, width=25)
        self.uni_valor.grid(row=8, column=1, padx=10, pady=8)

    def recomendation_show(self):
        analisis_btc = TA_Handler(
            symbol = "BTCUSDT",
            screener = "crypto",
            exchange = "BINANCE",
            interval = Interval.INTERVAL_1_MINUTE,
                )
        analisis_eth = TA_Handler(
            symbol = "ETHUSDT",
            screener = "crypto",
            exchange = "BINANCE",
            interval = Interval.INTERVAL_4_HOURS,
                )
        analisis_bnb = TA_Handler(
            symbol = "BNBUSDT",
            screener = "crypto",
            exchange = "BINANCE",
            interval = Interval.INTERVAL_4_HOURS,
                )
        analisis_xrp = TA_Handler(
            symbol = "XRPUSDT",
            screener = "crypto",
            exchange = "BINANCE",
            interval = Interval.INTERVAL_4_HOURS,
                )
        analisis_ada = TA_Handler(
            symbol = "ADAUSDT",
            screener = "crypto",
            exchange = "BINANCE",
            interval = Interval.INTERVAL_4_HOURS,
                )
        analisis_sol = TA_Handler(
            symbol = "SOLUSDT",
            screener = "crypto",
            exchange = "BINANCE",
            interval = Interval.INTERVAL_4_HOURS,
                )
        analisis_trx = TA_Handler(
            symbol = "TRXUSDT",
            screener = "crypto",
            exchange = "BINANCE",
            interval = Interval.INTERVAL_4_HOURS,
                )
        analisis_link = TA_Handler(
            symbol = "LINKUSDT",
            screener = "crypto",
            exchange = "BINANCE",
            interval = Interval.INTERVAL_4_HOURS,
                )
        analisis_uni = TA_Handler(
            symbol = "UNIUSDT",
            screener = "crypto",
            exchange = "BINANCE",
            interval = Interval.INTERVAL_4_HOURS,
                )

        recommendation_btc = analisis_btc.get_analysis().summary
        message_btc = recommendation_btc['RECOMMENDATION']
        self.btc_valor.config(text = message_btc)

        recommendation_eth = analisis_eth.get_analysis().summary
        message_eth = recommendation_eth['RECOMMENDATION']
        self.eth_valor.config(text = message_eth)

        recommendation_bnb = analisis_bnb.get_analysis().summary
        message_bnb = recommendation_bnb['RECOMMENDATION']
        self.bnb_valor.config(text = message_bnb)

        recommendation_xrp = analisis_xrp.get_analysis().summary
        message_xrp = recommendation_xrp['RECOMMENDATION']
        self.xrp_valor.config(text = message_xrp)

        recommendation_ada = analisis_ada.get_analysis().summary
        message_ada = recommendation_ada['RECOMMENDATION']
        self.ada_valor.config(text = message_ada)

        recommendation_sol = analisis_sol.get_analysis().summary
        message_sol = recommendation_sol['RECOMMENDATION']
        self.sol_valor.config(text = message_sol)

        recommendation_trx = analisis_trx.get_analysis().summary
        message_trx = recommendation_trx['RECOMMENDATION']
        self.trx_valor.config(text = message_trx)

        recommendation_link = analisis_link.get_analysis().summary
        message_link = recommendation_link['RECOMMENDATION']
        self.link_valor.config(text = message_link)

        recommendation_uni = analisis_uni.get_analysis().summary
        message_uni = recommendation_uni['RECOMMENDATION']
        self.uni_valor.config(text = message_uni)

        # Llamar a la función recomendation_show() cada 1 segundo
        self.window.after(1000, self.recomendation_show)

if __name__ == '__main__':
    print("Bot is running")
    ventana = Tk()
    application = Registro(ventana)
    application.recomendation_show()
    ventana.mainloop()

