import matplotlib.pyplot as plt
month = ['january', 'february', 'march', 'april', 'May', 'june',
         'july', 'august', 'september', 'october', 'november', 'december']
sales= [120, 135, 90, 150, 175, 160, 145, 170, 180, 190, 200, 210]

plt.plot(month,sales,marker="*",color="r")#markerle noktaları işaretledik
plt.xticks(rotation=45)#isimler sığmadığı için isimleri 45 derece dödürdük
plt.title("Aylık Satış Takibi")
plt.xlabel("Aylar")
plt.ylabel("Satış Miktarı")
plt.show()
