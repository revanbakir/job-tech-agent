import anthropic
import json
import os
from datetime import datetime
from dotenv import load_dotenv

# .env dosyasındaki API key'i yükle
load_dotenv()

# ─────────────────────────────────────────
# 1. İSTEM (PROMPT)
# ─────────────────────────────────────────
PROMPT = """
Türkiye'deki yazılım ve teknoloji sektöründe bu hafta açılan iş ilanlarını araştır.

Şunları bulmaya çalış:
- En çok ilan açılan alanlar (backend, frontend, devops, data science, mobile, siber güvenlik vb.)
- En çok aranan programlama dilleri ve teknolojiler (Python, Java, React, Kubernetes vb.)
- Hangi şehirlerde yoğunlaşıyor (İstanbul, Ankara, İzmir, remote vb.)
- Dikkat çeken bir trend varsa belirt

Kariyer.net, LinkedIn Türkiye, işkur.gov.tr veya benzeri kaynaklardan veri topla.

Sonuçları şu formatta ver:

## 📊 Bu Haftanın İş İlanı Trendleri

### 🏆 En Çok İlan Açılan Alanlar
(sıralı liste)

### 💻 En Çok Aranan Teknolojiler
(sıralı liste)

### 🗺️ Şehir Dağılımı
(kısa özet)

### 💡 Bu Haftanın Öne Çıkan Trendi
(1-2 cümle)
"""

# ─────────────────────────────────────────
# 2. API ÇAĞRISI
# ─────────────────────────────────────────
def analiz_yap():
    print("🔍 İş ilanları taranıyor, lütfen bekle...\n")

    client = anthropic.Anthropic()  # API key .env'den otomatik okunur

    # Web search tool ile mesaj gönder
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=3000,
        tools=[{"type": "web_search_20250305", "name": "web_search"}],
        messages=[{"role": "user", "content": PROMPT}]
    )

    # Cevabı metne çevir
    sonuc = ""
    for block in response.content:
        if hasattr(block, "text"):
            sonuc += block.text

    return sonuc

# ─────────────────────────────────────────
# 3. RAPORU KAYDET
# ─────────────────────────────────────────
def raporu_kaydet(sonuc):
    os.makedirs("raporlar", exist_ok=True)
    tarih = datetime.now().strftime("%Y-%m-%d")
    dosya_adi = f"raporlar/rapor_{tarih}.md"

    with open(dosya_adi, "w", encoding="utf-8") as f:
        f.write(f"# İş İlanı Trend Raporu — {tarih}\n\n")
        f.write(sonuc)

    print(f"✅ Rapor kaydedildi: {dosya_adi}")
    return dosya_adi

# ─────────────────────────────────────────
# 4. ANA PROGRAM
# ─────────────────────────────────────────
if __name__ == "__main__":
    sonuc = analiz_yap()

    print("=" * 60)
    print(sonuc)
    print("=" * 60)

    raporu_kaydet(sonuc)