import numpy as np
import matplotlib.pyplot as plt

dayList=["mon","tues","wed","thurs","friday","stdy","sunday"]
status=[27,19,25,27,28,28,29]

dayList_numpy=np.array(dayList)
status_numpy=np.array(status)

plt.plot(dayList_numpy,status_numpy,"b")#x ekseni,ye ekseni ve grafiğin rengi

plt.xlabel("Days")#x eksenin ismi
plt.ylabel("status")#y ekseninin ismi
plt.title("Van Weather Forecast")#başlık
plt.show()#grafiği göster
