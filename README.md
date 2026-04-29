# 📊 İş Piyasası Trend Analiz Ajanı

Claude AI kullanarak Türkiye'deki yazılım iş ilanlarını analiz eder.

## Kurulum

```bash
# 1. Gerekli paketleri yükle
pip install -r requirements.txt

# 2. API key'ini ayarla
# .env dosyasını aç, sk-ant-... kısmını kendi key'inle değiştir

# 3. Çalıştır
python main.py
```

## Nasıl Çalışır?

1. Claude'a web arama yetkisi verilir
2. Claude Kariyer.net, LinkedIn gibi siteleri tarar
3. Sonuçlar hem terminale yazdırılır hem `raporlar/` klasörüne kaydedilir

## Çıktı Örneği

```
# En Çok İlan Açılan Alanlar
1. Backend Developer
2. DevOps / Cloud
3. Frontend Developer
...
```