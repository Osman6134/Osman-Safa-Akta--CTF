import requests
import json

def ctf_verilerini_cek():
    # CTFtime API üzerinden yaklaşan 5 etkinliği çekiyoruz
    url = "https://ctftime.org/api/v1/events/?limit=5"
    
    # Güvenlik ve tanınma için User-Agent ekliyoruz
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) OSOP-CTF-Tracker'
    }
    
    print("--- [OSOP] CTF & Konferans Takip Sistemi Çalışıyor ---")
    
    try:
        response = requests.get(url, headers=headers)
        
        # JSON-first Parsing: Hocanın istediği veri işleme yöntemi
        if response.status_code == 200:
            events = response.json()
            for event in events:
                print(f"\n📌 Etkinlik: {event['title']}")
                print(f"📅 Başlangıç: {event['start']}")
                print(f"🔗 Detay: {event['url']}")
        else:
            print(f"⚠️ Veri çekilemedi. Hata kodu: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Bir bağlantı hatası oluştu: {e}")

if __name__ == "__main__":
    ctf_verilerini_cek()