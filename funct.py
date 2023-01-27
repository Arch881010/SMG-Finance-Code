from datetime import datetime as dt
today = dt.today().strftime('%Y.%m.%d(HR[%H])')
file = f'data\\{today}.txt'
dataw = open(file,'a')
import os
global leftover
def clear():
    os.system('cls')
def space(text):
    dataw.write(f"\n\nNew Data ^{text}\n\n")
def write(text):
    dataw.write(str(text))
def spent():
    logs = open("tickers\\total.txt",'r').readlines()
    names = []
    values = [0]
    shares = [0]
    x = -1
    y = 0
    alreadyspent = [0]
    while True:
        try:
            logs = logs
            name = logs[x+1]
            value = logs[x+2]
            share = logs[x+3]
            x=x+3
            names.append(name)
            values.append(value)
            shares.append(share)
            print(name, value, share, " group txt")
        except:
            break
    print(values,"values")
    for price in values:
        try: 
            alreadyspent[0] = int(alreadyspent[0]) + (int(values[y])*int(shares[y]))
            y = y + 1
        except:
            alreadyspent[0] = "ERROR"
    print(alreadyspent)
    return alreadyspent
def data():
    logs = open("tickers\\total.txt",'r').readlines()
    x = [0]
    names = []
    values = [0]
    shares = [0]
    spenttotal = [0]
    while True:
        try:
            #God: Get the value
            #Goal: Get the shares
            name = logs[x[0]]
            value = logs[x[0]+1]
            share = logs[x[0]+2]
            x[0] = x[0] + 2
            names.append(name)
            values.append(value)
            shares.appends(share)
            print(name, "name")
            print(value, "value")
            print(share, "share")
        except:
            break
    percent = 50
    percent = percent/100
    total = 100000
    MaxCap = total*percent
    spendable = (total-MaxCap)
    spentf = spent()
    spentcount = len(spentf)
    spentf = spentf[spentcount-1]
    y = [0]
    for value in values:
        #print(y[0])
        try:
            spenttotal[0] = spenttotal[0] + (int(value)*int(shares[y[0]]))
            y[0] = y[0] + 1
        except:
            pass
    try:
        leftover = (spendable-spentf)
    except:
        leftover = spendable
    leftover = round(leftover)
    return leftover

# Invest 85% or less.
# Today: 50%
# Buy at >$3.00 Share.
#>10 Shares
# Do not spend more than 20% of your money

