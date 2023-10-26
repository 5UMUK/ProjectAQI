# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Data_Set_PM2.5_ lung cancer.csv")
df

# %%
len(df[df["CO"].map(lambda x: x > 4000)])

# %%
df.drop(df[df["CO"] > 2000].index, axis=0, inplace=True)
df.shape
# %%

plt.scatter(df["CO"], df["PM2.5"], alpha=0.5)
plt.xlabel("CO")
plt.ylabel("PM2.5 ")
plt.show()
# %%
data = df.drop(["State", "County", "RT"], axis=1)
cor = data.corr()
cor
# %%

ax = sns.scatterplot(x="CO", y="PM2.5", data=data)
ax.set_title("CO vs. PM2.5")

# %%
sns.lmplot(x="CO", y="PM2.5", data=data)
# %%
cormat = data.corr()
round(cormat, 2)

# %%
plt.figure(figsize=(40,40))
sns.heatmap(cormat, annot=True, cmap='coolwarm')
# %%
