mystocks = {"TCS":123,"Infosys":987,"Idbi":890,"Ntpc":567}
#print(mystocks[0])
print(type(mystocks),mystocks)

mystocks["SBI"]=1344
print(mystocks)
print("no of stocks" ,len(mystocks))
#print(All stock name

    
for stock in mystocks.items():
    print(stock)
    print(stock[0],"has price", stock[1])

print("*"*40)
for stock, price in mystocks.items():
    print (stock , " has a price of ", price)

print("*"*40)

for stock in mystocks:
    print(stock,"has price", mystocks[stock])

print("*"*70)

mystocks.popitem()
print(mystocks)

print("*"*70)
del mystocks ["TCS"]
print(mystocks)


print("*"*70)
swapped = {}

for key,value in mystocks.items():
    swapped[value] = key
print(swapped)

print("*"*70)
print(*)































