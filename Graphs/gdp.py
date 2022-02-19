import requests
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

data_url = "https://raw.githubusercontent.com/ritza-co/datasets/master/gdp_data.csv"

r = requests.get(data_url)

with open("gdp-life.txt", "w") as f:
    f.write(r.text)

df = pd.read_csv("gdp-life.txt")
print(df.head())

print('___')
print('The correlation is: ', np.corrcoef(df['gdpPercap'], df['lifeExp']) [0, 1])
print('___')

sns.lmplot(
    'gdpPercap', 'lifeExp', df
).set_axis_labels('GDP per capita', 'Life Expectance')

plt.title('Countries with a higher GDP have higher life expectancy')
plt.tight_layout()
plt.show()
plt.savefig("GDP.png")