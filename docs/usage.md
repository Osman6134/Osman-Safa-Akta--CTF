# CTF Takip Sistemi - Kullanım Kılavuzu

Bu proje, CTFtime API'sini kullanarak yaklaşan siber güvenlik yarışmalarını terminal üzerinden listeler.

## Çalıştırma Talimatları
Sistemi çalıştırmak için terminale şu komutu yazın:
`python3 src/main.py`

## Özellikler
* **Otomatik Kontrol:** Sistem çalışmadan önce internet bağlantısını test eder.
* **Veri Formatı:** Veriler JSON formatında API'den çekilir ve parse edilir.
* **Hata Yönetimi:** Bağlantı hataları veya API sorunları kullanıcıya raporlanır.

## Gereksinimler
* Python 3.10 veya üzeri
* `requests` kütüphanesi (`pip install requests`)