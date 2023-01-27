nmlst = open('numlist.txt','a')
x = []
i = 0
while 99 > i:
    i = i + 1
    x.append(f"data\\values{i}.txt")

nmlst.write(str(x))