import json
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt  

with open("data.json", "r") as read_it: 
     data = json.load(read_it) 

DATA = []

for k in sorted(data['rates'].keys()):
    d = []
    d.append(k)
    d.append(data['rates'][k]['INR'])
    d.append(data['rates'][k]['GBP'])
    DATA.append(d)

exrates = pd.DataFrame(DATA)

with open("latest-rates.json", "r") as read_it: 
     latest = json.load(read_it) 

current_rates = []

current_rates.append(latest['rates']['INR'])
current_rates.append(latest['rates']['GBP'])

fig = plt.figure(figsize=(20,6))

ax1 = fig.add_axes([0, 0, 1, 1])

ax1.set_title('INR and GBP exchange rate against EUR')

ax1.plot(exrates[0],
         exrates[1],
         color='blue', label='Exchange rate for INR')

ax1.plot(exrates[0],
         exrates[2],
         color='green', label='Exchange rate for GBP')

plt.plot(0, current_rates[0], marker='o', markerfacecolor='blue', markersize=12, label='Cuurent rate for INR') 
plt.plot(0, current_rates[1], marker='o', markerfacecolor='green', markersize=12, label='Cuurent rate for GBP')
  
ax1.set_xlabel('Date')
ax1.set_ylabel('value')
ax1.legend()
ax1.xaxis.set_major_locator(plt.MaxNLocator(20))
plt.show()