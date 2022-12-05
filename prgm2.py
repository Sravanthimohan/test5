import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('mtcars.csv')
df.plot(kind = 'scatter', x = 'wt', y = 'mpg')
plt.show()

