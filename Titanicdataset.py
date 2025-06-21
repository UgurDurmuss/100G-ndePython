import pandas as pd
"""
Kaggle titanik veri seti
https://www.kaggle.com/datasets/yasserh/titanic-dataset?resource=download
"""

df=pd.read_csv('Titanic-Dataset.csv')
#dosyayı data frame de açtık

print(df.head())#DataFramin ilk 5 satırını okuduk
print(df.info())#Bu komut, sütunların veri türlerini, eksik değerleri ve toplam satır sayısını gösterir.
print(df.describe())#Bu komut, sayısal sütunlar için ortalamalar, standart sapmalar, min/max değerler gibi istatistiksel bilgileri gösterir.
print(df.shape)#Bu komut, veri setinin satır ve sütun sayısını gösterir.
# İlk 10 satır ve ilk 3 sütun
print(df.iloc[0:10, 0:3])
# "Name", "Age" ve "Fare" sütunlarını al
print(df.loc[:, ["Name", "Age", "Fare"]])

# 30 yaşın üzerindeki yolcular
print(df[df['Age'] > 30])

# Kadın yolcular
print(df[df['Sex'] == 'female'])

# 1. sınıf yolcular
print(df[df['Pclass'] == 1])
