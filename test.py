import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,10,1000)
y = np.sin(x)+1
z = np.cos(x**2)+1
plt.figure(figsize = (80,40))
plt.plot(x,y,label = '$\sin x+1$',color = 'red',linewidth = 2)
plt.plot(x,z,'b--',label = '$\cos x^2+1$')
plt.xlabel('Time(s) ')
plt.ylabel('Volt')
plt.title('Eg')
plt.ylim(0,2.2)
plt.legend()
plt.show()