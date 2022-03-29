
import matplotlib.pyplot as plt
import pandas as pd

# Define Data

data = {'Girls': [15, 20, 25, 30, 35],
        'Boys': [25, 30, 28, 19, 40] }
df = pd.DataFrame(data,columns=['Girls','Boys'], index = ['Team-1','Team-2','Team-3','Team-4','Team-5'])

# Multiple horizontal bar chart

df.plot.barh()

# Display

plt.show()