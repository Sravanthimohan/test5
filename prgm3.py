
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('mtcars.csv')
df["mpg"].plot(kind = 'bar')
plt.show()

