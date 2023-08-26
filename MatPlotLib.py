"""
The use of MatPlotLib to create a scatter plot from data in a Pandas DataFrame
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

housing = pd.DataFrame({'rooms':[1,1,2,2,2,3,3,3],  'price':[100,120,190,200,230,310,330,305]})

plt.scatter(housing['rooms'], housing['price'], color='red')  #x,y
plt.title('How house price varies with the number of rooms')
plt.xlabel('rooms')
plt.ylabel('price')
plt.show()