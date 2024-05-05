import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.animation import FuncAnimation
import utils
import numpy as numpy
import pandas as pd
import json


ITERATONS = 1000

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
theta0_desestandarizado = 0
theta1 = 0
theta1_desestandarizado = 0
theta0arr = []
theta1arr = []
learningRate = 0.01
size = len(data["km"])


plt.rcParams["figure.figsize"] = (16, 10)
plt.ion()
fig = plt.figure()


# ----- GRAPHIC -----
def draw_graphic():
    x = numpy.array(data.km)
    y = numpy.array(data.price)
    plt.subplot(1, 3, 1).remove()
    plt.subplot(1, 3, 1)
    plt.scatter(data.km, data.price)

    line_x = [0, data["km"].max()]
    line_y = [utils.estimate_price(0, theta0_desestandarizado, theta1_desestandarizado), utils.estimate_price(data["km"].max(), theta0_desestandarizado, theta1_desestandarizado)]
    plt.plot(line_x, line_y, linewidth=3, color="black")

    # plt.xticks(numpy.arange(0, ITERATONS))
    plt.xlabel("Mileage", fontsize=15, weight='bold')
    plt.ylabel("Price", fontsize=15, weight='bold')


# ----- GRAPHIC THETA0-----
def draw_theta0():
    plt.subplot(1, 3, 2).remove()
    plt.subplot(1, 3, 2)

    line_y = numpy.array(theta0arr)
    plt.plot(numpy.array(line_y), linewidth=3, color="black")

    plt.xticks(numpy.arange(0, ITERATONS, step=100))
    plt.yticks(numpy.arange(line_y.min(), 8500, step=500))
    plt.xlabel("Iterations", fontsize=15, weight='bold')
    plt.ylabel("Theta0", fontsize=15, weight='bold')


# ----- GRAPHIC THETA1-----
def draw_theta1():
    plt.subplot(1, 3, 3).remove()
    plt.subplot(1, 3, 3)

    line_x = numpy.array(theta1arr)
    y = []
    for i in range(len(theta1arr)):
        y.append(i)
    plt.plot(numpy.array(line_x), numpy.array(y), linewidth=3, color="black")

    plt.yticks(numpy.arange(0, ITERATONS, step=100))
    plt.xticks(numpy.arange(line_x.min(), 0.1, step=0.1))
    plt.xlabel("Iterations", fontsize=15, weight='bold')
    plt.ylabel("Theta1", fontsize=15, weight='bold')


def train():
    global theta0
    global theta0_desestandarizado
    global theta1
    global theta1_desestandarizado
    # ----- TRAIN -----
    for i in range(ITERATONS):
        D_t0 = 0
        D_t1 = 0
        for x in range(size):
            predicted = theta0 + (theta1 * s_data_km[x])
            D_t0 += predicted - s_data_price[x]
            D_t1 += (predicted - s_data_price[x]) * s_data_km[x]
        theta0 = theta0 - (learningRate * (1 / size) * D_t0)
        theta1 = theta1 - (learningRate * (1 / size) * D_t1)
        # ----- DESTANDARIZE DATA -----
        theta0_desestandarizado = mean_price + (theta0 * std_price / std_km) - (theta1 * mean_km * std_price / std_km)
        theta1_desestandarizado = theta1 * std_price / std_km
        theta0arr.append(theta0_desestandarizado)
        theta1arr.append(theta1_desestandarizado)
        draw_graphic()
        draw_theta0()
        draw_theta1()

        fig.canvas.draw()
        fig.canvas.flush_events()
        print("Theta0:", theta0_desestandarizado)
        print("Theta1:", theta1_desestandarizado)

    # ----- SEND THETA RESULT TO FILE -----
    with open("values.csv", "w") as f:
        f.write(json.dumps({'theta0': theta0_desestandarizado, 'theta1': theta1_desestandarizado}))


plt.rcParams["figure.figsize"] = (16, 10)
draw_graphic()
plt.suptitle("Data CSV", fontsize=22, weight='bold')
train()
plt.show()

