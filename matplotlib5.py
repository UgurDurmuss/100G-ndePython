import matplotlib.pyplot as plt
import  numpy as np

region=["marmara","doğu anadolu","akdeniz","Ege","Güneydoğu"]
population=[24,6,10,10,8]

region_numpy=np.array(region)
population_numpy=np.array(population)

plt.bar(region_numpy,population_numpy)#sutün grafiği
plt.title("Türkiye Bölgesel nüfus dağılımı")
plt.xlabel("bölgeler")
plt.ylabel("nüfus")
plt.show()
