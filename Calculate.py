import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.widgets import Button
import json
import numpy
from matplotlib.widgets import TextBox
import pandas as pd
import utils
import os

theta0 = 0
theta1 = 0

def get_theta_values():
    try:
        f = open("values.csv", "r")
        file = json.load(f)
        print(file)
        global theta0
        theta0 = file["theta0"]
        global theta1
        theta1 = file["theta1"]
    except:
        print("The program is not trained")
        #os.system("python3 Train.py")


get_theta_values()

# ----- READ DATA CSV -----
data = pd.read_csv("data.csv")
new_values_x = [""]
new_values_y = [""]

def draw_table():
    # ----- CSV TABLE -----
    plt.subplot(2, 2, 1)
    plt.axis('off') #changes x and y axis limits such that all data is shown
    table = plt.table(cellText=data.values, colLabels=data.columns, rowLoc='center', cellLoc='center', loc='center')
    table.scale(1, 1.1)

    # Set Colum title to BOLD
    for (row, col), cell in table.get_celld().items():
        if (row == 0):
            cell.set_text_props(fontproperties=FontProperties(weight='bold'))


# ----- GRAPHIC -----
def draw_graphic():
    x = numpy.array(data.km)
    y = numpy.array(data.price)
    plt.subplot(2, 2, 2).remove()
    plt.subplot(2, 2, 2)
    plt.scatter(data.km, data.price)

    line_x = [0, data["km"].max()]
    line_y = [utils.estimate_price(0, theta0, theta1), utils.estimate_price(data["km"].max(), theta0, theta1)]
    plt.plot(line_x, line_y, linewidth=3, color="black")

    plt.xticks(numpy.arange(0, 300000, step=50000))
    plt.xlabel("Mileage", fontsize=15, weight='bold')
    plt.ylabel("Price", fontsize=15, weight='bold')


# ----- DRAWTABLE FOR NEW VALUES -----
def draw_new_values():
    plt.subplot(2, 2, 3).remove()
    plt.subplot(2, 2, 3)
    plt.axis('off') #changes x and y axis limits such that all data is shown
    values = pd.DataFrame(data=numpy.c_[new_values_x, new_values_y])
    table = plt.table(cellText=values.values, colLabels=["km", "price"], rowLoc='center', cellLoc='center', loc='center')
    table.scale(1, 1.1)

    # Set Colum title to BOLD
    for (row, col), cell in table.get_celld().items():
        if (row == 0):
            cell.set_text_props(fontproperties=FontProperties(weight='bold'))


# ----- INPUT -----
def submit(text: str):
    global text_box
    text = text_box.text
    if not text.isnumeric() or float(text) >= 396283 or float(text) <= 0:
        text_box.set_val("")
        return
    new_y: float = theta0 + (theta1 * float(text))
    plt.subplot(2, 2, 2)
    plt.scatter(float(text), new_y, color="red", s=80)
    plt.draw()
    global new_values_x
    global new_values_y
    
    text_box.set_val("")
    new_values_x.append(text)
    new_values_y.append(str(round(new_y, 2)))
    if new_values_x.__contains__(""):
        new_values_x.remove("")
        new_values_y.remove("")
    draw_new_values()


def train(val):
    os.system("python3 Train.py")
    get_theta_values()
    draw_graphic()
    plt.draw()
    # exit()


def add_input_box():
    plt.subplot(2, 2, 4).remove()
    ax = plt.subplot(2, 2, 4)
    ax.axis('off')

    info:str = ""
    info += "estimatePrice(mileage) = θ0 + (θ1 ∗ mileage)\n\n"
    info += r'Theta0 = learningRate * ' + r'$\frac{1}{m}$ ' + r'$\sum_{i=0}^{m-1} (estimatePrice(mileage[i] - price[i]))$' + "\n"
    info += r'Theta1 = learningRate * ' + r'$\frac{1}{m}$ ' + r'$\sum_{i=0}^{m-1} (estimatePrice(mileage[i] - price[i]) * mileage[i])$' + "\n\n\n"
    info += "Theta0: " + str(theta0) + "\n"
    info += "Theta1: " + str(theta1) + "\n"
    ax.text(0, 0.3, info, fontsize=9, verticalalignment='bottom', horizontalalignment='left')



plt.rcParams["figure.figsize"] = (12, 10)
fig = plt.figure()
draw_graphic()
draw_table()
draw_new_values()
add_input_box()
plt.suptitle("Linear Regression", fontsize=22, weight='bold')

fig.tight_layout()

axbox = plt.axes([0.7, 0.1, 0.1, 0.035])
text_box = TextBox(axbox, 'Insert mileage to calculate price:  ')
# text_box.on_submit(submit)

# axbtn = plt.axes([0.7, 0.91, 0.1, 0.035])
btnCalculate = Button(plt.axes([0.81, 0.1, 0.1, 0.035]), 'Calculate')
btnCalculate.on_clicked(submit)

btnTrain = Button(plt.axes([0.5, 0.05, 0.08, 0.035]), 'Train')
btnTrain.on_clicked(train)

fig.canvas.draw()
fig.canvas.flush_events()

def on_close(event):
    exit()
fig.canvas.mpl_connect('close_event', on_close)

try:
    plt.show()
except KeyboardInterrupt:
    exit()