import pandas as pd
import matplotlib.pyplot as plt
DF = pd.read_csv("https://raw.githubusercontent.com / fivethirtyeight / data / master / airline-safety / airline-safety.csv")
x = list(DF.aorline-safety-management)
plt.boxplot(x)
plt.show()

