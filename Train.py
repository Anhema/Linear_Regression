import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import csv
import numpy
import utils

theta0 = 0
theta1 = 0

header = []
rows = []

with open('data.csv', mode='r') as file:
    csvFile = csv.reader(file)
    header = next(csvFile)
    for row in csvFile:
        rows.append(row)

print(header)
print(rows)

plt.rcParams["figure.figsize"] = (18, 11)

# ----- Data table -----
plt.subplot(1, 2, 1)
plt.axis('tight') #turns off the axis lines and labels
plt.axis('off') #changes x and y axis limits such that all data is shown
table = plt.table(cellText=rows, colLabels=header, rowLoc='center', cellLoc='center', loc='center')
table.scale(1, 2)

# Set Colum title to BOLD
for (row, col), cell in table.get_celld().items():
    if (row == 0):
        cell.set_text_props(fontproperties=FontProperties(weight='bold'))

# ----- Graphic -----
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
plt.xlabel("Mileage", weight='bold')
plt.ylabel("Price", weight='bold')

plt.suptitle("Data CSV", weight='bold')
plt.show()
