import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.animation import FuncAnimation
import utils
import numpy as numpy
import pandas as pd
import json

# ----- READ DATA -----
data = pd.read_csv("data.csv")

mean_km = utils.mean(data["km"])
std_km = utils.standard_derivation(data["km"])
mean_price = utils.mean(data["price"])
std_price = utils.standard_derivation(data["price"])


# ----- STANDARIZE DATA -----
s_data_km = (data["km"] - mean_km) / std_km
s_data_price = (data["price"] - mean_price) / std_price



theta0 = 0
theta1 = 0
learningRate = 0.001
size = len(data["km"])

for i in range(10000):
    D_t0 = 0
    D_t1 = 0
    for x in range(size):
        predicted = theta0 + (theta1 * s_data_km[x])
        D_t0 += predicted - s_data_price[x]
        D_t1 += (predicted - s_data_price[x]) * s_data_km[x]
    theta0 = theta0 - (learningRate * (1 / size) * D_t0)
    theta1 = theta1 - (learningRate * (1 / size) * D_t1)
    # draw_graphic()


# ----- DESTANDARIZE DATA -----
theta0_desestandarizado = mean_price + (theta0 * std_price / std_km) - (theta1 * mean_km * std_price / std_km)
theta1_desestandarizado = theta1 * std_price / std_km


print("Theta0:", theta0_desestandarizado)
print("Theta1:", theta1_desestandarizado)


# ----- SEND THETA RESULT TO FILE -----
with open("values.csv", "w") as f:
    f.write(json.dumps({'theta0': theta0_desestandarizado, 'theta1': theta1_desestandarizado}))
