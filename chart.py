import matplotlib.pyplot as plt
import csv
import pandas as pd

df = pd.read_csv("data_cleaned - data_cleaned.csv")

mass =df["star_mass"].tolist()
radius = df["star_radius"].tolist()
dist = df["Dist"].tolist()

mass.sort()
radius.sort()


plt.plot(radius,mass)
plt.title("Radiuses and Masses of Stars")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()

plt.plot(mass,radius)

plt.title("Mass & Radius")
plt.xlabel("Mass")
plt.show()

plt.scatter(radius,mass)
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()
