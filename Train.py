import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import utils
import numpy as numpy
import pandas as pd
import json
import os


ITERATONS = 1000
LEARNINGRATE = 0.01
DRAWINTERVAL = 10
STOPPERCENTAJE = 0.00001

# ----- DELETE CURREN FILE IF EXIST -----
if os.path.exists("values.csv"):
  os.remove("values.csv")


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
lossarr = []
losslist = []
size = len(data["km"])

trainingFinished: bool = False

try:
    plt.rcParams["figure.figsize"] = (16, 9)
    plt.ion()
    fig = plt.figure()
except KeyboardInterrupt:
    exit()

def on_close(event):
    exit()
fig.canvas.mpl_connect('close_event', on_close)

# ----- GRAPHIC -----
def draw_graphic():
    x = numpy.array(data.km)
    y = numpy.array(data.price)
    plt.subplot(2, 3, 2).remove()
    plt.subplot(2, 3, 2)
    plt.scatter(data.km, data.price)

    line_x = [0, data["km"].max()]
    line_y = [utils.estimate_price(0, theta0_desestandarizado, theta1_desestandarizado), utils.estimate_price(data["km"].max(), theta0_desestandarizado, theta1_desestandarizado)]
    plt.plot(line_x, line_y, linewidth=3, color="black")

    # plt.xticks(numpy.arange(0, ITERATONS))
    plt.xlabel("Mileage", fontsize=15, weight='bold')
    plt.ylabel("Price", fontsize=15, weight='bold')


# ----- GRAPHIC THETA0-----
def draw_theta0():
    plt.subplot(2, 3, 4).remove()
    plt.subplot(2, 3, 4)

    line_y = numpy.array(theta0arr)
    plt.plot(numpy.array(line_y), linewidth=3, color="black")

    plt.xticks(numpy.arange(0, ITERATONS + 100, step=ITERATONS / 10))
    plt.yticks(numpy.arange(line_y.min(), 9500, step=500))
    plt.xlabel("Iterations", fontsize=15, weight='bold')
    plt.ylabel("Theta0", fontsize=15, weight='bold')


# ----- GRAPHIC THETA1-----
def draw_theta1():
    plt.subplot(2, 3, 5).remove()
    plt.subplot(2, 3, 5)

    line_x = numpy.array(theta1arr)
    y = []
    for i in range(len(theta1arr)):
        y.append(i)
    plt.plot(numpy.array(y), numpy.array(line_x), linewidth=3, color="black")

    plt.xticks(numpy.arange(0, ITERATONS + 100, step=ITERATONS / 10))
    plt.yticks(numpy.arange(-0.025, 0, step=0.005))
    plt.xlabel("Iterations", fontsize=15, weight='bold')
    plt.ylabel("Theta1", fontsize=15, weight='bold')


# ----- GRAPHIC LOSS -----
def draw_loss():
    plt.subplot(2, 3, 6).remove()
    plt.subplot(2, 3, 6)

    line_x = numpy.array(lossarr)
    y = []
    for i in range(len(lossarr)):
        y.append(i)
    plt.plot(numpy.array(y), numpy.array(line_x), linewidth=3, color="black")

    plt.xticks(numpy.arange(0, ITERATONS + 100, step=ITERATONS / 10))
    plt.yticks(numpy.arange(0, 3, step=0.5))
    plt.xlabel("Iterations", fontsize=15, weight='bold')
    plt.ylabel("LOSS", fontsize=15, weight='bold')


# ----- DRAW TABLE -----
def draw_table():
    plt.subplot(2, 3, 1).remove()
    plt.subplot(2, 3, 1)
    plt.axis('off') #changes x and y axis limits such that all data is shown
    table = plt.table(cellText=data.values, colLabels=data.columns, rowLoc='center', cellLoc='center', loc='center')
    table.scale(1, 1.1)

    # Set Colum title to BOLD
    for (row, col), cell in table.get_celld().items():
        if (row == 0):
            cell.set_text_props(fontproperties=FontProperties(weight='bold'))


# ----- INFO-----
def draw_info(iteration: int):
    plt.subplot(2, 3, 3).remove()
    ax = plt.subplot(2, 3, 3)
    ax.axis('off')
    if trainingFinished:
        ax.set_title('Training Finished', fontsize=14, fontweight='bold', color="green")
    else:
        ax.set_title('Training in progress', fontsize=14, fontweight='bold', color="red")
    
    info:str = ""
    info += "Learning Rate: " + str(LEARNINGRATE) + "\n"
    info += "Max Iterations: " + str(ITERATONS) + "\n"
    info += "Refresh iterations: " + str(DRAWINTERVAL) + "\n"
    info += "Stop Percentaje: " + str(STOPPERCENTAJE) + "%\n\n\n"
    info += "Iteration: " + str(iteration) + "\n"
    info += "Loss: " + str(lossarr[len(lossarr) - 1]) + "\n"
    info += "Theta0: " + str(theta0_desestandarizado) + "\n"
    info += "Theta1: " + str(theta1_desestandarizado) + "\n\n\n\n"
    info += "estimatePrice(mileage) = θ0 + (θ1 ∗ mileage)\n\n"
    info += r'Theta0 = learningRate * ' + r'$\frac{1}{m}$ ' + r'$\sum_{i=0}^{m-1} (estimatePrice(mileage[i] - price[i]))$' + "\n"
    info += r'Theta1 = learningRate * ' + r'$\frac{1}{m}$ ' + r'$\sum_{i=0}^{m-1} (estimatePrice(mileage[i] - price[i]) * mileage[i])$' + "\n"
    ax.text(-0.2, -0.05, info, fontsize=9, verticalalignment='bottom', horizontalalignment='left')


def show_metrics(i: int):
    try:
        draw_graphic()
        draw_theta0()
        draw_theta1()
        draw_loss()
        draw_info(i)
        draw_table()
        fig.tight_layout()
        fig.canvas.draw()
        fig.canvas.flush_events()
    except KeyboardInterrupt:
        exit()


def train():
    global theta0
    global theta0_desestandarizado
    global theta1
    global theta1_desestandarizado
    global trainingFinished
    # ----- TRAIN -----
    for i in range(1, ITERATONS + 1):
        D_t0 = 0
        D_t1 = 0
        loss = 0
        for x in range(size):
            predicted = theta0 + (theta1 * s_data_km[x])
            loss = predicted - s_data_price[x]
            D_t0 += predicted - s_data_price[x]
            D_t1 += (predicted - s_data_price[x]) * s_data_km[x]
        if len(losslist) > 1:
            percent = abs((loss ** 2) - losslist[len(losslist) - 1]) / losslist[len(losslist) - 1]
            if percent <= STOPPERCENTAJE:
                trainingFinished = True
                break;
        losslist.append(loss ** 2)
        lossarr.append(utils.mean(losslist))
        theta0 = theta0 - (LEARNINGRATE * (1 / size) * D_t0)
        theta1 = theta1 - (LEARNINGRATE * (1 / size) * D_t1)
        # ----- DESTANDARIZE DATA -----
        theta0_desestandarizado = mean_price + (theta0 * std_price / std_km) - (theta1 * mean_km * std_price / std_km)
        theta1_desestandarizado = theta1 * std_price / std_km
        theta0arr.append(theta0_desestandarizado)
        theta1arr.append(theta1_desestandarizado)
        # ----- DRAW EVERY 5 ITERATIONS -----
        if i % DRAWINTERVAL == 0:
            show_metrics(i)

    trainingFinished = True
    show_metrics(ITERATONS)
   
        # print("Theta0:", theta0_desestandarizado)
        # print("Theta1:", theta1_desestandarizado)

    # ----- SEND THETA RESULT TO FILE -----
    with open("values.csv", "w") as f:
        f.write(json.dumps({'theta0': theta0_desestandarizado, 'theta1': theta1_desestandarizado}))

plt.suptitle("TRAINING LINEAR REGRESSION", fontsize=22, weight='bold')
train()

try:
    plt.show(block=True)
except KeyboardInterrupt:
    exit()
