import matplotlib.pyplot as plt
import seaborn as sns

df=sns.load_dataset("iris")
sns.lineplot(data=df,y="sepal_length",x=df.index,hue="species")

plt.xlabel("Indexes")
plt.ylabel("Sepal length")

plt.legend(title='Species', loc='upper left', labels=['setosa', 'versicolor','virginica'])

plt.savefig("iris-lineplot")
#plt.show()