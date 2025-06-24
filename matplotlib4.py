import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-10,10,1)#-10 dan 10 a 1 er adımlarla sayılar
y=2*x*x+1
plt.plot(x,y,"b*-")# mavi ve yıldız artı düz çizgilerle devam edecek
plt.show()
