# 🛡️ Zerguz Trojan & Ransomware Detection System

> **Canary Token mantığı ile çalışan gerçek zamanlı Trojan ve Ransomware
> tespit sistemi**

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-success)
![Status](https://img.shields.io/badge/Durum-Aktif-brightgreen)

------------------------------------------------------------------------

# 📖 Proje Hakkında

**Zerguz Trojan & Ransomware Detection System**, Python ile
geliştirilmiş davranış tabanlı bir güvenlik aracıdır.

Program, klasik antivirüslerin aksine imza tabanlı çalışmak yerine
**Canary Folder (Tuzak Klasör)** yaklaşımını kullanır. Zararlı yazılımın
ilk hedeflerinden biri olması beklenen sahte dosyaları izler ve şüpheli
bir hareket algıladığı anda alarm üretir, olay kaydı oluşturur ve isteğe
bağlı olarak sistemi ağdan izole eder.

------------------------------------------------------------------------

# 🎯 Temel Özellikler

-   ✅ Gerçek zamanlı dosya sistemi izleme
-   ✅ Canary Folder oluşturma
-   ✅ Sahte kritik dosyalar üretme
-   ✅ Dosya değiştirme tespiti
-   ✅ Dosya silme tespiti
-   ✅ Dosya taşıma / yeniden adlandırma tespiti
-   ✅ Ransomware uzantı analizi
-   ✅ Otomatik log oluşturma
-   ✅ Windows ve Linux desteği
-   ✅ Otomatik ağ izolasyonu

------------------------------------------------------------------------

# ⚙️ Çalışma Mantığı

Program başlatıldığında otomatik olarak **Önemli-Raporlar** isimli bir
klasör oluşturur.

İçerisine aşağıdaki gibi sahte dosyalar eklenir:

``` text
Muhasebe_2024_Rapor.xlsx
Personel_Maas_Bilgileri.docx
Yedek_Sifreler.txt
Proje_Sozlesmesi.pdf
```

Program bu klasörü gerçek zamanlı izler.

Aşağıdaki olaylardan biri gerçekleşirse saldırı olarak değerlendirilir:

-   Dosya değiştirilmesi
-   Dosyanın silinmesi
-   Dosyanın taşınması
-   Dosyanın yeniden adlandırılması
-   Şüpheli uzantıya dönüştürülmesi

------------------------------------------------------------------------

# 🚨 Desteklenen Şüpheli Uzantılar

``` text
.enc
.locked
.crypt
.crypted
.encrypted
.ransom
.locky
.cerber
.wcry
.wncry
.zzz
.xyz
.crypto
.ezz
.exx
.r5a
.vault
```

------------------------------------------------------------------------

# 🌐 Otomatik Ağ İzolasyonu

Saldırı algılandığında program:

## Windows

-   IP yapılandırmasını serbest bırakır.
-   Ağ arayüzlerini listeler.
-   Aktif adaptörleri devre dışı bırakır.

## Linux

-   Loopback harici ağ arayüzlerini kapatır.

> Bu özellik yönetici/root yetkisi gerektirebilir.

------------------------------------------------------------------------

# 📝 Loglama

Tüm olaylar:

``` text
zerguz_events.log
```

dosyasına kaydedilir.

Loglarda;

-   Tarih
-   Saat
-   Alarm sebebi
-   Ağ izolasyonu
-   Hata kayıtları

bulunmaktadır.

------------------------------------------------------------------------

# 📂 Proje Yapısı

``` text
Zerguz/
│
├── Zerguz-Trojen-Tespit.py
├── zerguz_events.log
└── Önemli-Raporlar/
    ├── Muhasebe_2024_Rapor.xlsx
    ├── Personel_Maas_Bilgileri.docx
    ├── Yedek_Sifreler.txt
    └── Proje_Sozlesmesi.pdf
```

------------------------------------------------------------------------

# 📦 Kurulum

``` bash
git clone https://github.com/KULLANICI_ADI/REPO.git

cd REPO

pip install watchdog colorama
```

------------------------------------------------------------------------

# ▶️ Kullanım

``` bash
python Zerguz-Trojen-Tespit.py
```

Program otomatik olarak:

1.  Tuzak klasörü oluşturur.
2.  Sahte dosyaları üretir.
3.  İzleme moduna geçer.
4.  Şüpheli davranışları takip eder.
5.  Alarm oluşursa log üretir.
6.  Ağ izolasyonunu başlatır.

------------------------------------------------------------------------

# 🔄 İş Akışı

``` text
Program Başlatılır
        │
        ▼
Canary Klasörü Oluştur
        │
        ▼
Dosya Sistemini İzle
        │
        ▼
Şüpheli Davranış?
   │             │
 Hayır         Evet
   │             │
   ▼             ▼
İzlemeye      Alarm Ver
 Devam Et        │
                 ▼
          Log Dosyası Oluştur
                 │
                 ▼
          Ağ İzolasyonunu Başlat
```

------------------------------------------------------------------------

# 💻 Kullanılan Teknolojiler

-   Python
-   Watchdog
-   Colorama
-   Logging
-   Subprocess
-   Datetime
-   OS

------------------------------------------------------------------------

# 🎯 Kullanım Alanları

-   SOC Analistleri
-   Blue Team
-   Incident Response
-   Malware Analizi
-   Siber Güvenlik Eğitimleri
-   Üniversite Projeleri

------------------------------------------------------------------------

# 🚧 Gelecek Sürümler

-   VirusTotal API
-   Telegram Bildirimleri
-   Discord Bildirimleri
-   HTML Raporlama
-   SIEM Entegrasyonu
-   MITRE ATT&CK Eşleştirmesi
-   Süreç Sonlandırma
-   Web Arayüzü
-   Çoklu Canary Klasörü

------------------------------------------------------------------------

# ⚠️ Sorumluluk Reddi

Bu proje yalnızca eğitim, araştırma ve savunma amaçlı geliştirilmiştir.

------------------------------------------------------------------------

# 👨‍💻 Geliştirici

**Malikejder Durgun**

SOC Analyst • Blue Team • Python • Cyber Security
