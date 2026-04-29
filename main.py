import anthropic
import os
from datetime import datetime
from dotenv import load_dotenv
from dashboard import html_rapor_olustur

load_dotenv()

PROMPT = """
Türkiye'deki yazılım ve teknoloji sektöründe bu hafta açılan iş ilanlarını araştır.

Şunları bulmaya çalış:
- En çok ilan açılan alanlar (backend, frontend, devops, data science, mobile, siber güvenlik vb.)
- En çok aranan programlama dilleri ve teknolojiler (Python, Java, React, Kubernetes vb.)
- Hangi şehirlerde yoğunlaşıyor (İstanbul, Ankara, İzmir, remote vb.)
- Dikkat çeken bir trend varsa belirt

Kariyer.net, LinkedIn Türkiye veya benzeri kaynaklardan veri topla.

Sonuçları şu formatta ver:

## Bu Haftanın Is Ilani Trendleri

### En Cok Ilan Acilan Alanlar
(siralı liste)

### En Cok Aranan Teknolojiler
(siralı liste)

### Sehir Dagilimi
(kisa ozet)

### Bu Haftanin One Cikan Trendi
(1-2 cumle)
"""


def analiz_yap():
    print("Is ilanlari taranıyor, lutfen bekle...\n")
    client = anthropic.Anthropic()

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=3000,
        tools=[{"type": "web_search_20250305", "name": "web_search"}],
        messages=[{"role": "user", "content": PROMPT}]
    )

    sonuc = ""
    for block in response.content:
        if hasattr(block, "text"):
            sonuc += block.text

    return sonuc


def kaydet(sonuc, tarih):
    os.makedirs("raporlar", exist_ok=True)

    md_dosya = f"raporlar/rapor_{tarih}.md"
    with open(md_dosya, "w", encoding="utf-8") as f:
        f.write(f"# Is Ilani Trend Raporu - {tarih}\n\n")
        f.write(sonuc)
    print(f"Markdown kaydedildi: {md_dosya}")

    html_dosya = f"raporlar/rapor_{tarih}.html"
    with open(html_dosya, "w", encoding="utf-8") as f:
        f.write(html_rapor_olustur(sonuc, tarih))
    print(f"HTML dashboard kaydedildi: {html_dosya}")
    print(f"\nTarayicida ac: {os.path.abspath(html_dosya)}")


if __name__ == "__main__":
    tarih = datetime.now().strftime("%Y-%m-%d")
    sonuc = analiz_yap()

    print("=" * 60)
    print(sonuc)
    print("=" * 60 + "\n")

    kaydet(sonuc, tarih)