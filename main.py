import yfinance as yf
from funct import *
i = -1
tckdlist = []
fetchedtickerlist = open("tickers\\tickerlist.txt", "r").read()
tickerlist = list(fetchedtickerlist.split(", "))
print(tickerlist)
leftover = data()
for ticker in tickerlist:
    tckdlist.append(yf.Ticker(ticker))
clear()
time = dt.today().strftime('%Y-%m-%d %H:%M:%S')
dataw.write("\n\n" + time + " was when this data was requested.")
for ticker in tickerlist:
    i = i + 1
    data = yf.download(
        tickers = ticker,
        period = "ytd",
        interval = "1d",
        ignore_tz = False,
        group_by = 'column',
        auto_adjust = True,
        repair = False,
        prepost = True,
        threads = True,
        proxy = None
    )
    writeabledata = data#['MSFT']
    write("\n \nTicker: "+str(ticker)+"\n")
    write(writeabledata)
    #write(f"\n revenue_forecasts for" + str(tckdlist[i].info)+'\n \n')
    dataw.flush()
print(f"${leftover} is the spendable value.")
    