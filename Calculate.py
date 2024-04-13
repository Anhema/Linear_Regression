import matplotlib.pyplot as plt
import numpy
import utils

print(utils.mean([99,86,87,88,111,86,103,87,94,78,77,85,86]))
print(utils.median([99,86,87,88,111,86,103,87,94,78,77,85,86]))
print(utils.mode([99,86,87,88,111,86,103,87,94,78,77,85,86]))
print(utils.standard_derivation([32,111,138,28,59,77,97]))
print(utils.percentile([5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31], 75))

# Cambiar la resolucion de la pantalla al iniciar
plt.rcParams["figure.figsize"] = (18, 11)


# plot 1:
x = [0, 1, 2, 3]
y = [3, 8, 1, 10]

plt.subplot(2, 3, 1)
plt.scatter(x,y)  # scatter pone puntos sin unir
plt.xlabel("Valor X-1")
plt.ylabel("Valor Y-1")
plt.title("Grafico 1")
plt.grid()

# plot 2:
x = [0, 1, 2, 3]
y = [10, 20, 30, 40]

plt.subplot(2, 3, 2)
plt.plot(x, y)  # plot une los puntos formando una linea
plt.xlabel("Valor X-2")
plt.ylabel("Valor Y-2")
plt.title("Grafico 2")
plt.grid()

# plot 3:
x = numpy.random.uniform(0.0, 5.0, 1000)

plt.subplot(2, 3, 3)
plt.hist(x, 10)
plt.xlabel("Valor X-3")
plt.ylabel("Valor Y-3")
plt.title("Grafico 3")
plt.grid()

# plot 4:
x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.subplot(2, 3, 4)
plt.scatter(x, y)  # plot une los puntos formando una linea
plt.xlabel("Valor X-4")
plt.ylabel("Valor Y-4")
plt.title("Grafico 4")
plt.grid()

# plot 5:
x = numpy.random.normal(5.0, 1.0, 100000)

plt.subplot(2, 3, 5)
plt.hist(x, 100)
plt.xlabel("Valor X-5")
plt.ylabel("Valor Y-5")
plt.title("Grafico 5")
plt.grid()

plt.suptitle("MY GRAPHS")

plt.show()
