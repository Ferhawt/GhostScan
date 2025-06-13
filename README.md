# GhostScan: OSINT Destekli Siber Tehdit Tespiti ve Haritalama Aracı

GhostScan, açık kaynak istihbarat (OSINT) yöntemleriyle hedef sistemler hakkında bilgi toplayan ve temel zafiyet analizi gerçekleştiren bir siber güvenlik araştırma projesidir.

## 🔎 Projenin Amacı

- OSINT (Open Source Intelligence) araçlarını entegre ederek hedef sistemler hakkında bilgi toplamak.
- Nmap ve özel Python betikleri kullanarak temel zafiyet taraması yapmak.
- Toplanan verileri görselleştirerek analiz kolaylığı sağlamak.
- Red Team bakış açısı kazandırmak ve etik hacking prensiplerine uygun çalışmak.

## 🚀 Özellikler

- Shodan API ile geniş veri toplama
- Google Dorks entegrasyonu
- Nmap ile port ve servis taraması
- Python ile temel zafiyet kontrol betikleri
- NetworkX ile temel topoloji haritalandırma ve görselleştirme

## 🛠️ Kullanılan Teknolojiler

- Python (Requests, BeautifulSoup, socket, NetworkX)
- Nmap / Zenmap
- Shodan API
- Google Dorks
- Matplotlib

## 🔧 Kurulum

1. Repoyu klonla:
```bash
git clone https://github.com/kullanici_adin/GhostScan.git
cd GhostScan
