import matplotlib.pyplot as plt
import numpy

x = numpy.linspace(-numpy.pi, numpy.pi, 100)
y = numpy.sin(x)

plt.plot(x, y)
plt.title("Test")
plt.xlabel("x-coordinate")
plt.ylabel("y-coordinate")
plt.show()

