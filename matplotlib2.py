import matplotlib.pyplot as plt
notes = 'ali', 'hasan', 'mesut', 'cengiz'#bu bir tuple
sizes = [15, 30, 45, 10]

fig, ax = plt.subplots()#fig dediğimiz şey pencere ax ise bu pencerenin içinde bulunan grafik objesi
ax.pie(sizes, labels=notes)#sizes her dilimin büyüklüğü,labels dilimlerin ütüne yazılacak isimler
plt.show()#her grafiği göstermek için bunu yapmak zorundayız
