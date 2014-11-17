####################PIECEWISE FUNCTION EXAMPLE######################
#			-Created by Felipe Novais & Estela Mello-
#		-Dedicated to Renato Cantao great guy and teacher-
#
####################################################################

#IMPORTS
import matplotlib.pyplot as plt
from numpy import arange

#VARIABLES
x = arange(-2, 0, 0.0001)
x2 = arange(0, 2, 0.0001)
x3 = arange(2, 4, 0.0001)
y = 2*(x**2)
y2 = 5+(-1*(x2**2))
y3 = (x3+2)
dotx = [0, 2]
doty = [5, 4]
circlex = [0, 2]
circley = [0, 1]

#PLOTING
plt.plot(x, y, 'b', x2, y2, 'b', x3, y3, 'b')
plt.plot([-2,-2], [0,8], 'k--', [0,0], [0,5], 'k--', [2,2], [0,4], 'k--', [4,4], [0,6], 'k--')
plt.text(-2.1 , -0.3, 'a')
plt.text(3.9 , -0.3 , 'b')
plt.scatter(circlex, circley, s=30, c='b', edgecolors='b')
plt.scatter(dotx, doty, s=30, c='w', edgecolors='b')

#SHOWING
plt.grid()
plt.show()
