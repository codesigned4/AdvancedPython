import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df=sns.load_dataset("iris")

data=df.groupby(by="species").mean()["sepal_length"]
ax=sns.barplot(x=data.index,y=data.values)
ax.set_title("Sepal Length Means")
ax.set_ylabel("Mean")

figure=ax.get_figure()
figure.savefig("Sepal-Length-Means")
#plt.show()