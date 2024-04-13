import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import csv
import numpy
from matplotlib.widgets import TextBox
import utils

theta0 = 0
theta1 = 0
learningRate = 0.001

header = []
rows = []

with open('data.csv', mode='r') as file:
    csvFile = csv.reader(file)
    header = next(csvFile)
    for row in csvFile:
        rows.append(row)

def calculate_theta0():
    sum: float = 0
    for row in rows:
        sum += (int(row[0]) - int(row[1]))

    theta0 = learningRate * 1/len(rows) * sum
    return theta0


def calculate_theta1():
    sum: float = 0
    for row in rows:
        sum += (float(row[0]) - float(row[1])) * float(row[0])

    theta1 = learningRate * 1 / len(rows) * sum
    return theta1

theta0 = calculate_theta0()
theta1 = calculate_theta1()
print(theta0)
print(theta1)

plt.rcParams["figure.figsize"] = (18, 11)

# ----- CSV TABLE -----
plt.subplot(1, 2, 1)
plt.axis('tight') #turns off the axis lines and labels
plt.axis('off') #changes x and y axis limits such that all data is shown
table = plt.table(cellText=rows, colLabels=header, rowLoc='center', cellLoc='center', loc='center')
table.scale(1, 2)

# Set Colum title to BOLD
for (row, col), cell in table.get_celld().items():
    if (row == 0):
        cell.set_text_props(fontproperties=FontProperties(weight='bold'))


# ----- GRAPHIC -----
plt.rcParams['figure.figsize'] = (10, 6)

km = []
price = []
for row in rows:
    km.append(row[0])
    price.append(row[1])

x = numpy.array(km)
y = numpy.array(price)
plt.subplot(1, 2, 2)
plt.scatter(x, y)
plt.xticks(numpy.arange(0, len(rows), step=3))
plt.xlabel("Mileage", fontsize=15, weight='bold')
plt.ylabel("Price", fontsize=15, weight='bold')


# ----- INPUT -----
def submit(text):
    print(text)

axbox = plt.axes([0.4, 0.9, 0.2, 0.035])
text_box = TextBox(axbox, 'Calculate price')
text_box.on_submit(submit)


plt.suptitle("Data CSV", fontsize=22, weight='bold')
plt.show()