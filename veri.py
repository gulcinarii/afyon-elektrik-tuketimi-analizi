import pandas as pd

df = pd.read_excel("pivot.xls")
print(df.head())
import pandas as pd

# Excel dosyasını oku
df = pd.read_excel("pivot.xls")

# İlk 3 gereksiz satırı (0, 1 ve 2. satırları) atıp, sadece son iki sütunu (Yıl ve Tüketim) alalım
df_temiz = df.iloc[3:, [2, 3]].copy()

# Sütun isimlerini anlaşılır şekilde değiştirelim
df_temiz.columns = ["Yil", "Elektrik_Tuketimi_Kwh"]

# Boş (NaN) satırlar varsa temizleyelim ve Yıl sütununu tam sayıya çevirelim
df_temiz = df_temiz.dropna()
df_temiz["Yil"] = df_temiz["Yil"].astype(int)
df_temiz["Elektrik_Tuketimi_Kwh"] = pd.to_numeric(df_temiz["Elektrik_Tuketimi_Kwh"])

# Satır numaralarını 0'dan başlayacak şekilde sıfırlayalım
df_temiz = df_temiz.reset_index(drop=True)

# Temizlenmiş tablonun tamamını ekrana yazdıralım
print(df_temiz)
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.plot(df_temiz["Yil"], df_temiz["Elektrik_Tuketimi_Kwh"], marker="o", color="b", linewidth=2)
plt.title("Yıllara Göre Kişi Başına Elektrik Tüketimi (Kwh)")
plt.xlabel("Yıl")
plt.ylabel("Elektrik Tüketimi (Kwh)")
plt.grid(True)
# 1. Temiz veriyi CSV veya Excel olarak kaydet
df_temiz.to_csv("afyon_elektrik_tuketimi_temiz.csv", index=False, encoding="utf-8-sig")

# 2. Grafiği yüksek çözünürlüklü resim (PNG) olarak kaydet (plt.show'dan ÖNCE yazılmalı!)
plt.savefig("elektrik_tuketim_grafigi.png", dpi=300, bbox_inches="tight")

plt.show()

df_temiz.to_excel("temiz_elektrik_verisi.xlsx", index=False)
print("Temiz Excel dosyası başarıyla kaydedildi!")