import matplotlib.pyplot as plt
import numpy

#plot 1:
x = [0, 1, 2, 3]
y = [3, 8, 1, 10]

plt.subplot(2, 2, 1)
plt.scatter(x,y) #scatter pone puntos sin unir
plt.xlabel("Valor X-1")
plt.ylabel("Valor Y-1")
plt.title("Grafico 1")
plt.grid()

#plot 2:
x = [0, 1, 2, 3]
y = [10, 20, 30, 40]

plt.subplot(2, 2, 2)
plt.plot(x,y) #plot une los puntos formando una linea
plt.xlabel("Valor X-2")
plt.ylabel("Valor Y-2")
plt.title("Grafico 2")
plt.grid()

#plot 3:
x = [0, 1, 2, 3]
y = [10, 20, 30, 40]

plt.subplot(2, 2, 3)
plt.plot(x,y) #plot une los puntos formando una linea
plt.xlabel("Valor X-3")
plt.ylabel("Valor Y-3")
plt.title("Grafico 3")
plt.grid()

#plot 4:
x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.subplot(2, 2, 4)
plt.scatter(x,y) #plot une los puntos formando una linea
plt.xlabel("Valor X-4")
plt.ylabel("Valor Y-4")
plt.title("Grafico 4")
plt.grid()

plt.suptitle("MY GRAPHS")
plt.show()
