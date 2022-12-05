import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('mtcars.csv')
df.boxplot(by ='cyl', column =['mpg'])
plt.show()

