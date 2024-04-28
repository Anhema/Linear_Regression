import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import csv
import numpy
from matplotlib.widgets import TextBox
import pandas as pd
import utils

theta0 = 0
theta1 = 0

# ----- READ DATA CSV -----
data = pd.read_csv("data.csv")

def estimate_price(x: int):
    return theta0 + (theta1 * x)

def draw_table():
    # ----- CSV TABLE -----
    plt.subplot(1, 2, 1)
    plt.axis('tight') #turns off the axis lines and labels
    plt.axis('off') #changes x and y axis limits such that all data is shown
    table = plt.table(cellText=data.values, colLabels=data.columns, rowLoc='center', cellLoc='center', loc='center')
    table.scale(1, 2)

    # Set Colum title to BOLD
    for (row, col), cell in table.get_celld().items():
        if (row == 0):
            cell.set_text_props(fontproperties=FontProperties(weight='bold'))


# ----- GRAPHIC -----
def draw_graphic():
    x = numpy.array(data.km)
    y = numpy.array(data.price)
    plt.subplot(1, 2, 2)
    plt.scatter(data.km, data.price)

    line_x = [0, data["km"].max()]
    line_y = [estimate_price(0), estimate_price(data["km"].max())]
    plt.plot(line_x, line_y, linewidth=3, color="black")

    # plt.xticks(numpy.arange(0, len(data.km), step=3))
    plt.xlabel("Mileage", fontsize=15, weight='bold')
    plt.ylabel("Price", fontsize=15, weight='bold')


# ----- INPUT -----
def submit(text: str):
    if not text.isnumeric():
        return
    print(text)
    new_y: int = theta0 + (theta1 * int(text))
    # km.append(int(text))
    # price.append(new_y)
    plt.subplot(1, 2, 2)
    plt.scatter(int(text), new_y, color="red", s=80)


def add_input_box():
    axbox = plt.axes([0.7, 0.91, 0.1, 0.035])
    text_box = TextBox(axbox, 'Calculate price  ')
    text_box.on_submit(submit)


plt.rcParams["figure.figsize"] = (16, 10)
draw_graphic()
draw_table()

axbox = plt.axes([0.7, 0.91, 0.1, 0.035])
text_box = TextBox(axbox, 'Calculate price  ')
text_box.on_submit(submit)

plt.suptitle("Data CSV", fontsize=22, weight='bold')
plt.show()
