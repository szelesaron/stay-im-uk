import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

os.chdir(r"C:\Users\Áron\Google Drive\Dokumentumok\Skócia")
data = pd.read_csv(r"stay-in-uk.csv")
data.dropna()


l = []
d = []
for i in range(360, len(data)):
    if np.sum(data["In UK"][i-360:i]) < 180:
        l.append(i-360)
        d.append(data["Date"][i-360])


print(f"Dates: {d}")

#red line represents the start of the 360 day period in which residency was less than 180 days
zeros = [0]*len(l)
plt.figure(figsize=(10,5))
plt.plot(data["In UK"])
plt.plot(l,zeros, color = "red")
plt.title("Days spent in the UK")
plt.xlabel("Days")
plt.ylabel("In UK 0/1")
plt.show()