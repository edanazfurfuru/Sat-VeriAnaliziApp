# Adım Adım Proje Geliştirme Rehberi

Bu dosya, oluşturduğumuz Satış Analizi projesinin mantığını, kodların ne işe yaradığını ve nasıl çalıştığını adım adım anlatmak için hazırlanmıştır. Python ile veri analizi öğrenim sürecinizde kaynak olarak kullanabilirsiniz.

## 1. Hazırlık ve Kütüphaneler

Veri analizi yaparken standart haline gelmiş bazı kütüphanelere ihtiyacımız vardır. `analysis.py` dosyasının en başında bunları içe aktardık:

```python
import pandas as pd           # Veri işleme ve tablo işlemleri için (Excel gibi düşünün)
import numpy as np            # Matematiksel işlemler için
import matplotlib.pyplot as plt # Grafikleri çizdirmek için
import os                     # Dosya ve klasör yönetimi için (örn. output klasörü yaratmak)
import random                 # Rastgele sayı ve veri üretmek için
from datetime import datetime, timedelta # Tarih işlemleri için
```

**Neden?**
- `pandas`: "DataFrame" adı verilen yapıları sayesinde veriyi satır-sütun (tablo) formatında tutar ve filtrelemeyi çok kolaylaştırır.
- `matplotlib`: Veriyi görselleştirmek (çizgi grafik, pasta grafik vb.) için kullanılır.

## 2. Veri Üretimi (Data Generation)

Gerçek bir verimiz olmadığı için, `generate_data` fonksiyonu ile simülasyon yaptık.

```python
def generate_data():
    categories = ['Electronics', 'Clothing', ...] # Ürün kategorilerimiz
    
    # 1000 satırlık rastgele veri üretiyoruz
    for _ in range(1000):
        # Rastgele tarih seç (1 yıl içinden)
        date = start_date + timedelta(days=random.randint(0, 365))
        # Rastgele kategori ve bölge seç
        category = random.choice(categories)
        # 10 ile 500 arasında rastgele satış tutarı belirle
        sales_amount = round(random.uniform(10.0, 500.0), 2)
        ...
```

**Mantık:**
Boş bir liste oluşturup, bir döngü (loop) içinde her satır için rastgele değerler seçip listeye ekledik. Sonunda bu listeyi `df = pd.DataFrame(data)` diyerek Pandas tablosuna çevirdik ve `sales_data.csv` olarak kaydettik.

## 3. Veri Analizi (Data Analysis)

Veriyi anlamlandırmak için `analyze_data` fonksiyonunu yazdık. Burada Pandas'ın gücünü kullandık.

### Aylık Satışlar (`resample`)
```python
# Veriyi 'Date' sütununa göre indeksliyoruz ve 'M' (Month) bazında gruplayıp topluyoruz.
monthly_sales = df.set_index('Date').resample('M')['Sales_Amount'].sum()
```
Bu kod satırı, binlerce satırlık veriyi aylara bölüp her ayın toplam satışını hesaplar.

### Kategori Bazlı Satış (`groupby`)
```python
# Kategoriye göre grupla ve topla
category_sales = df.groupby('Category')['Sales_Amount'].sum()
```
Bu kod, "Electronics ne kadar sattı?", "Clothing ne kadar sattı?" sorularının cevabını verir.

## 4. Görselleştirme (Visualization)

`create_visualizations` fonksiyonunda `matplotlib` kullanarak analiz sonuçlarını grafiğe döktük.

```python
plt.figure(figsize=(10, 6)) # Grafik boyutu (genişlik, yükseklik)
analysis_results['monthly_sales'].plot(kind='line', marker='o') # Çizgi grafik çiz
plt.title('Monthly Sales Trend') # Başlık
plt.savefig(f"{OUTPUT_DIR}/monthly_sales.png") # Dosyaya kaydet
plt.close() # Hafızayı temizle
```

**İpucu:** `kind='line'` çizgi grafik, `kind='bar'` sütun grafik, `kind='pie'` ise pasta grafik çizer.

## 5. Raporlama (HTML Generation)

Son olarak, bu grafikleri ve sayısal sonuçları birleştirip şık bir rapor oluşturmak istedik. `generate_html_report` fonksiyonu bunu yapar.

Burası aslında Python içinde **HTML kodu yazmaktan** ibarettir. "f-string" (f"...") yapısını kullanarak Python değişkenlerini HTML içine gömdük.

```python
html_content = f"""
...
<div class="metric-value">${metrics['total_revenue']}</div>
...
<img src="output/monthly_sales.png">
...
"""
```

Bu sayede dinamik bir rapor oluşur. Kod her çalıştığında veriler değişse bile rapor otomatik güncellenir.

## Nasıl Çalışır?

`main` fonksiyonu orkestra şefi gibidir:

1. `generate_data()` çalıştır -> Veriyi üret.
2. `analyze_data()` çalıştır -> Veriyi analiz et.
3. `create_visualizations()` çalıştır -> Grafikleri çiz.
4. `generate_html_report()` çalıştır -> Raporu yaz.

## Kendini Geliştirmek İçin Öneriler

Bu kod üzerinde pratik yapmak istersen şunları deneyebilirsin:
1.  **Yeni Veri Ekle**: `generate_data` kısmına 'Profit' (Kar) adında yeni bir sütun ekle.
2.  **Yeni Grafik Çiz**: Bölgelere göre satışları (Region) gösteren bir sütun grafik ekle.
3.  **Excel Çıktısı**: Veriyi CSV yerine Excel olarak kaydet (`df.to_excel("satislar.xlsx")`).
