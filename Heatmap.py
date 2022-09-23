import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("new_earthquake.csv")
data = data.drop(["id", "date", "dir"], axis=1)
g = sns.heatmap(data.corr(), center=0)
g.set_title("Heatmap of Earthquake Variables")
plt.show()
