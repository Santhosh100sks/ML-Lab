import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("icbhi_dataset.csv")

crackle = data["crackle"].astype(int)
wheeze = data["wheeze"].astype(int)

classes = ((crackle + wheeze) > 0).astype(int)

plt.figure(figsize=(6,6))

for i in range(len(X)):
    if classes[i] == 0:
        plt.scatter(X[i], Y[i], color="blue")
    else:
        plt.scatter(X[i], Y[i], color="red")

plt.xlabel("mfcc0")
plt.ylabel("mfcc1")
plt.title("Scatter Plot using Crackle & Wheeze Classes")
plt.show()