import pandas as pd

df=pd.read_csv("GBvideos.csv")

#İlk 10 kaydı alınız
result=df.head(10)

#İkinci 5 kaydı alınız
result=df[5:10]

#Datasette bulunan kolon isimlerini ve sayılarını bulunuz
result=df.columns
result=len(df.columns)

#Belirtilen columnları silmek için drop methodu kullanılır
#df.drop(["column1","column2",axis=1]) axis=1 de column olarak silineceğini belirtir
#orijinal frame içerisinde değişiklik yapmak için inplace="True" parametresini drop methodu içerisine yollamayı unutma

#Like Dislike sayılarının ortalamasını bulunuz
result=df["likes"].mean()
result=df["dislikes"].mean()

#İlk 50 videonun like ve disile columnlarını getiriniz
result=df.head(50)[["title","likes","dislikes"]]

#En çok görüntülenen video hangisidir?
result=df[df["views"].max()==df["views"]]["title"].iloc[0]

#En fazla görüntülenen ilk 10 video hangisidir
result=df.sort_values("views",ascending=False).head(10)[["title","views"]]

#Kategoriye göre beğeni ortlamarını sıralır bir şekilde getiriniz
result=df.groupby("category_id").mean().sort_values("likes")["likes"]

#Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız
result=df.groupby("category_id").sum().sort_values("comment_count",ascending=False)["comment_count"]

#Her kategoride kaç video vardır
result=df["category_id"].value_counts()

#Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz
df["title_len"]=df["title"].apply(len)

#Her video için kullanılan tag sayısını yeni bir column da gösteriniz
df["tag_count"]=df["tags"].apply(lambda x:len(x.split("|")))
result=df


print(result)