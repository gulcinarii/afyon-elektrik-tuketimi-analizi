#  Afyonkarahisar Kişi Başı Elektrik Tüketimi Analizi (2000 - 2024)

> TÜİK Merkezi Dağıtım Sistemi (MEDAS) verileri kullanılarak gerçekleştirilen, ham verinin temizlenmesinden görselleştirilmesine kadar uçtan uca (End-to-End) Python veri analizi projesi.

---

##  Proje Hakkında
Bu çalışmada, Türkiye İstatistik Kurumu (TÜİK) verileri taban alınarak Afyonkarahisar ilinin 2000 ile 2024 yılları arasındaki **kişi başına düşen toplam elektrik tüketimi (kWh)** trendleri incelenmiştir. Amaç; ham ve düzensiz bir veri setini programatik olarak temizlemek, pandas kütüphanesiyle analize uygun hale getirmek ve matplotlib ile anlamlı bir görsel içgörü elde etmektir.

---

##  Kullanılan Teknolojiler ve Kütüphaneler
* **Python 3.15**
* **Pandas** (Veri manipülasyonu, temizliği ve dönüştürme işlemleri)
* **Matplotlib** (Zaman serisi görselleştirme ve grafik çizimi)
* **Xlrd** (Eski tip `.xls` Excel uzantılarının okunması)

---

##  Veri Ön İşleme ve Temizleme Adımları (`Data Cleaning`)
TÜİK'ten `.xls` formatında indirilen ham veri setinde karşılaşılan yapısal zorluklar şu adımlarla çözülmüştür:
1. **Gereksiz Başlıkların Ayıklanması:** Tablonun üst kısmındaki meta veriler ve boşluk satırları `iloc` fonksiyonu ile filtrelendi.
2. **Eksik Değer Yönetimi:** `NaN` (boş) hücreler veri setinden arındırıldı.
3. **Tip Dönüşümleri:** Yıl sütunu `integer` (tam sayı) formatına, tüketim değerleri ise sayısal analiz yapılabilmesi için uygun veri tipine dönüştürüldü.

---

##  Veri Görselleştirme ve Temel Bulgular
25 yıllık periyodu kapsayan analiz sonucunda elde edilen grafik reponun içinde `elektrik_tuketim_grafigi.png` olarak yer almaktadır. 

* **Genel Trend:** 2000 yılında **951 kWh** olan kişi başı elektrik tüketimi, yıllar içinde düzenli bir artış eğilimi göstererek 2024 yılında **2890 kWh** seviyesine ulaşmıştır (yaklaşık 3 kat artış).

---

   ```bash
   git clone [https://github.com/kullaniciadin/afyon-elektrik-tuketimi-analizi.git](https://github.com/kullaniciadin/afyon-elektrik-tuketimi-analizi.git)
