import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(rc={"figure.figsize":(22,22)}) #seaborn figure size ını ayarlıyoruz

df=pd.read_csv("world-happiness-report.csv")
plt.title("Correlation Matrix")
sns.heatmap(df.corr(),annot=True,linewidths=.5)
plt.savefig("Correlation-heatmap.png")