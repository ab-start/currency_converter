with open('python1') as f:
    lines=f.readlines()
currency={}
for line in lines:
    parsed=line.split('\t')
    currency[parsed[0]]=parsed[1]
amount=int(input('enter amount:\n'))
print('here the available currency to convert:')
for item in currency.keys():
    print(item)
curren=input('enter the name of currency u wanna to convert')
print(f"{amount} INR is equal to {amount*float(currency[curren])} {curren}")




