import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import csv
import numpy
from matplotlib.widgets import TextBox
import utils
import pandas as pd

# Theta0 = 8400
# Theta1 = -0.02
theta0: float = 0
theta1: float = 0
learningRate = 0.001

data = pd.read_csv("data.csv")


def estimate_price(x: int):
    return theta0 + (theta1 * x)


def calculate_theta0():
    sum: float = 0
    for row in data.values:
        sum += estimate_price(int(row[0]) - int(row[1]))

    theta0 = learningRate * 1/len(data.values) * sum
    return theta0


def calculate_theta1():
    sum: float = 0
    for row in data.values:
        sum += estimate_price((float(row[0]) - float(row[1])) * float(row[0]))

    theta1 = learningRate * 1 / len(data.values) * sum
    return theta1


theta0 = calculate_theta0()
theta1 = calculate_theta1()
print(theta0)
print(theta1)