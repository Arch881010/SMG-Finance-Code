from funct import *
leftover = data()
print(f"${leftover} spendable.")
tickername = input("Ticker Name? ")
tickervalue = input("Bought Price? ")
tickershares = input("How many shares? ")
add = open("tickers\\total.txt",'a')
add.writeLines(f"{tickername.upper()}")
add.write(f"{tickervalue}")
add.write(f"{tickershares}")

