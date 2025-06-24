import matplotlib.pyplot as plt
import  numpy as np

region=["marmara","doğu anadolu","akdeniz","Ege","Güneydoğu"]
population=[24,6,10,10,8]

region_numpy=np.array(region)
population_numpy=np.array(population)

plt.subplot(1,2,1)#1 satır iki sutün olacak şekilde iki tane yan yana grafik yerleşirdik
plt.bar(region_numpy,population_numpy)#sutün grafiği
plt.title("Türkiye Bölgesel nüfus dağılımı")
plt.xlabel("bölgeler")
plt.ylabel("nüfus")
plt.xticks(rotation=45)


plt.subplot(1,2,2)
plt.plot(region_numpy,population_numpy,"r*-")
plt.xticks(rotation=45)
plt.show()

plt.show()
