import pandas as pd

data=pd.read_csv("nba.csv")
#ilk 10 kayıt
result=data.head(10)

#Toplam kayıt sayısı
result=len(data.index)

#Tüm oyuncuların toplam maaş ortalaması
result=data["Salary"].mean()

#En yüksek maaş
result=data["Salary"].max()

#En yüksek maaşı alan oyuncu kimdir
result=data[data["Salary"]==data["Salary"].max()]["Name"]

#Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı getiriniz
result=data[(data["Age"] >=20) & (data["Age"] <25)][["Name","Team","Age"]].sort_values("Age",ascending=False)

#John Holland isimli oyuncunun oynadığı takım hangisidir
result=data[data["Name"]=="John Holland"]["Team"].iloc[0]

#Takımlara göre oyuncuların ortalama maaş bilgilerini alınız
result=data.groupby("Team").mean()["Salary"]

#Kaç farklı takım mevcuttur
result=len(data.groupby("Team"))
#veya
result=data["Team"].nunique()#unique de her birinden bir adet olan liste gelir 

#Her takımda kaç oyuncu oynamaktadır
result=data["Team"].value_counts()

#Adı içerisinde "and" geçen kayıtları bulunuz
result=data[data["Name"].str.contains("and")]

print(result)