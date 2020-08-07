import pandas as pd
from texttable import Texttable
import matplotlib.pyplot as plt  

dataset1 = pd.read_csv('btc.csv')

# part 1 task
dataset2 = {'Date' : dataset1.Date[len(dataset1)-365 : len(dataset1)], 
            'Volume' : dataset1.Volume[len(dataset1)-365 : len(dataset1)], 
            'LowEuro' : dataset1.Low[len(dataset1)-365 : len(dataset1)] * 0.87, 
            'HighEuro' : dataset1.High[len(dataset1)-365 : len(dataset1)] * 0.87}
dataset2 = pd.DataFrame(dataset2, columns = ['Date', 'Volume' , 'LowEuro' , 'HighEuro'])
dataset2.to_csv('output.csv')

#part 2 task
data = [["\t", "min" , "max" , "mean"],
        ["Low (Euro) ", dataset2['LowEuro'].min() , dataset2['LowEuro'].max() , dataset2['LowEuro'].mean()],
        ["High (Euro) ", dataset2['HighEuro'].min() , dataset2['HighEuro'].max() , dataset2['HighEuro'].mean()],
        ["Volume (Billions)" , dataset2['Volume'].min()/1000000000 , dataset2['Volume'].max()/1000000000 , dataset2['Volume'].mean()/1000000000 ]]
table = Texttable()
table.add_rows(data)
print(table.draw())

#part 3 task
plt.plot( dataset2['Date'] , dataset2['LowEuro'] , label = "LowEuro / Date")
plt.plot( dataset2['Date' ] , dataset2['HighEuro'] , label = "HighEuro / Date")
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Line Chart of the Bitcoin price (Low & High) in the past year')
plt.legend()
plt.show()