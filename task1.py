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
    DATA.append(d)

exrates = pd.DataFrame(DATA)

fig = plt.figure(figsize=(20,6))

ax1 = fig.add_axes([0, 0, 1, 1])

ax1.set_title('EUR to INR')

ax1.plot(exrates[0],
         exrates[1],
         color='blue', label='exchange rate')

ax1.set_xlabel('Date')
ax1.set_ylabel('value')
ax1.legend()
ax1.xaxis.set_major_locator(plt.MaxNLocator(20))
plt.show()