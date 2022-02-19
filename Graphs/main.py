from matplotlib import pyplot as plt
import requests
import random

data_url = "https://raw.githubusercontent.com/sixhobbits/ritza/master/data/us-cities.txt"

r = requests.get(data_url)

with open("us-cities.txt", "w") as f:
    f.write(r.text)

lats = []
lons = []
colors = []
state_colors = {}

all_colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

with open("Graphs/us-cities.txt") as f:
    for i, line in enumerate(f):
        state, lat, lon = line.split()
        lats.append(float(lat))
        lons.append(float(lon))

        #Assign states a random color
        if state not in state_colors:
            state_colors[state] = random.choice(all_colors)
        colors.append(state_colors[state])

plt.scatter(lons, lats, c = colors)
plt.show()


