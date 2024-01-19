import numpy as np
import matplotlib.pyplot as plt
fig,ax=plt.subplots()
ax.set_xlim((-5,5)) # interval of x axis
ax.set_ylim((-5,5)) # interval of y axis
ax.grid() #setka
ax.set_xlabel("x")
ax.set_ylabel("y")
x = np.linspace(-6,6,400) 
ax.plot(x,x**3 +3*x - 1,label=r'$f(x)=\ x**3 +3*x -1$')
ax.plot(x, x*0, 0.001)
ax.legend(loc='best', fontsize=7)
plt.savefig('figure_with_legend.png')
plt.show()