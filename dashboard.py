"""
Analiz sonucunu güzel bir HTML dashboard'a çevirir.
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>İş Trend Raporu — {tarih}</title>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: system-ui, sans-serif; background: #f5f5f5; color: #1a1a1a; padding: 2rem; }}
    h1 {{ font-size: 22px; font-weight: 500; margin-bottom: 0.25rem; }}
    .subtitle {{ font-size: 14px; color: #666; margin-bottom: 2rem; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-bottom: 2rem; }}
    .metric {{ background: #fff; border-radius: 10px; padding: 1rem 1.25rem; border: 1px solid #e5e5e5; }}
    .metric-label {{ font-size: 12px; color: #888; margin-bottom: 4px; }}
    .metric-value {{ font-size: 24px; font-weight: 500; }}
    .card {{ background: #fff; border-radius: 12px; padding: 1.25rem; border: 1px solid #e5e5e5; margin-bottom: 1.5rem; }}
    .card h2 {{ font-size: 12px; font-weight: 500; color: #888; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1rem; }}
    .analiz {{ white-space: pre-wrap; font-size: 14px; line-height: 1.7; color: #333; }}
    footer {{ font-size: 12px; color: #aaa; text-align: center; margin-top: 2rem; }}
  </style>
</head>
<body>
  <h1>İş Piyasası Trend Raporu</h1>
  <p class="subtitle">{tarih} tarihli analiz — Türkiye yazılım sektörü</p>

  <div class="card">
    <h2>Bu haftanın analizi</h2>
    <div class="analiz">{analiz}</div>
  </div>

  <footer>Claude AI tarafından oluşturuldu — job-tech-agent</footer>
</body>
</html>"""


def html_rapor_olustur(analiz: str, tarih: str) -> str:
    return HTML_TEMPLATE.format(tarih=tarih, analiz=analiz)