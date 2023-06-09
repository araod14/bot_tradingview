from tradingview_ta import TA_Handler,Interval

symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT", "ADAUSDT", "SOLUSDT", "TRXUSDT", "LINKUSDT", "UNIUSDT"]

for symbol in symbols:
    analisis = TA_Handler(
        symbol=symbol,
        screener="crypto",
        exchange="BINANCE",
        interval=Interval.INTERVAL_4_HOURS,
        # proxies={'http': 'http://example.com:8080'} # Uncomment to enable proxy (replace the URL).
        )
    print(symbol,analisis.get_analysis().summary)