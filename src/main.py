import requests
import json
import sys

def sistem_kontrol():
    # Adım 7: Auto Control Ability - İnternet ve API erişim testi
    print("--- [Sistem Kontrolü Başlatılıyor] ---")
    try:
        requests.get("https://8.8.8.8", timeout=3)
        print("✅ İnternet Bağlantısı: OK")
        return True
    except:
        print("❌ Hata: İnternet bağlantısı yok!")
        return False

def ctf_verilerini_cek():
    if not sistem_kontrol():
        return

    url = "https://ctftime.org/api/v1/events/?limit=5"
    headers = {'User-Agent': 'Mozilla/5.0 OSOP-CTF-Tracker'}
    
    try:
        response = requests.get(url, headers=headers)
        # Adım 7: JSON-first Parsing
        if response.status_code == 200:
            events = response.json()
            print(f"\n✅ Veri Çekme Başarılı: {len(events)} etkinlik bulundu.")
            for event in events:
                print(f"📌 {event['title']} | {event['start']}")
        else:
            print(f"⚠️ Sunucu Hatası: {response.status_code}")
    except Exception as e:
        print(f"💥 Kritik Hata: {e}")

if __name__ == "__main__":
    ctf_verilerini_cek()