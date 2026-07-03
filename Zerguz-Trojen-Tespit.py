#!/usr/bin/env python3

import os
import sys
import time
import platform
import subprocess
import logging
from datetime import datetime

try:
    from colorama import init as colorama_init, Fore, Back, Style
except ImportError:
    print("colorama bulunamadı. Kurulum: pip install colorama")
    sys.exit(1)

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ImportError:
    print("watchdog bulunamadı. Kurulum: pip install watchdog")
    sys.exit(1)

colorama_init(autoreset=True)

CANARY_DIR = "Önemli-Raporlar"       
LOG_FILE = "zerguz_events.log"             
SUSPICIOUS_EXTENSIONS = {                   
    ".enc", ".locked", ".crypt", ".crypted", ".encrypted",
    ".ransom", ".locky", ".cerber", ".wcry", ".wncry", ".zzz",
    ".xyz", ".crypto", ".ezz", ".exx", ".r5a", ".vault",
}

ENABLE_REAL_NETWORK_KILL = True

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def banner():
    art = f"""{Fore.RED}{Style.BRIGHT}
     ███████╗███████╗██████╗  ██████╗ ██╗   ██╗███████╗
     ╚══███╔╝██╔════╝██╔══██╗██╔════╝ ██║   ██║╚══███╔╝
       ███╔╝ █████╗  ██████╔╝██║  ███╗██║   ██║  ███╔╝
      ███╔╝  ██╔══╝  ██╔══██╗██║   ██║██║   ██║ ███╔╝
     ███████╗███████╗██║  ██║╚██████╔╝╚██████╔╝███████╗
     ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝
    {Style.RESET_ALL}{Fore.YELLOW}{Style.BRIGHT}
          >> Ransomware Defender - Canary Token EDR <<
    {Style.RESET_ALL}{Fore.CYAN}
     -----------------------------------------------------
      Tuzak Klasör : {Style.RESET_ALL}{Fore.WHITE}{CANARY_DIR}{Style.RESET_ALL}{Fore.CYAN}
      Log Dosyası  : {Style.RESET_ALL}{Fore.WHITE}{LOG_FILE}{Style.RESET_ALL}{Fore.CYAN}
      İşletim Sist.: {Style.RESET_ALL}{Fore.WHITE}{platform.system()}{Style.RESET_ALL}{Fore.CYAN}
      Ağ İzolasyonu: {Style.RESET_ALL}{Fore.WHITE}{"AKTİF" if ENABLE_REAL_NETWORK_KILL else "SİMÜLASYON (kapalı)"}{Style.RESET_ALL}{Fore.CYAN}
     -----------------------------------------------------
    {Style.RESET_ALL}
    """
    print(art)


def ensure_canary_dir():
    if not os.path.exists(CANARY_DIR):
        os.makedirs(CANARY_DIR)
        decoy_files = [
            "Muhasebe_2024_Rapor.xlsx",
            "Personel_Maas_Bilgileri.docx",
            "Yedek_Sifreler.txt",
            "Proje_Sozlesmesi.pdf",
        ]
        for fname in decoy_files:
            with open(os.path.join(CANARY_DIR, fname), "w", encoding="utf-8") as f:
                f.write("Kendini çok mu akıllı sanıyorsun sen :).\n")
        print(f"{Fore.GREEN}[+] Tuzak klasör oluşturuldu ve sahte dosyalarla dolduruldu: "
              f"{CANARY_DIR}{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}[i] Tuzak klasör zaten mevcut: {CANARY_DIR}{Style.RESET_ALL}")


def print_alarm(reason: str):
    msg = "ALARM: ZERGUZ RANSOMWARE TESPİT ETTİ - AĞ BAĞLANTISI KESİLDİ!"
    bar = "!" * len(msg)
    print(f"\n{Back.RED}{Fore.WHITE}{Style.BRIGHT}{bar}{Style.RESET_ALL}")
    print(f"{Back.RED}{Fore.WHITE}{Style.BRIGHT}{msg}{Style.RESET_ALL}")
    print(f"{Back.RED}{Fore.WHITE}{Style.BRIGHT}{bar}{Style.RESET_ALL}")
    print(f"{Fore.RED}[SEBEP] {reason}{Style.RESET_ALL}")
    print(f"{Fore.RED}[ZAMAN] {datetime.now().isoformat()}{Style.RESET_ALL}\n")
    logging.warning(f"RANSOMWARE ALARMI - Sebep: {reason}")


def isolate_network():
    system = os.name  

    if not ENABLE_REAL_NETWORK_KILL:
        print(f"{Fore.YELLOW}[SİMÜLASYON] Gerçek ağ kesme işlemi devre dışı "
              f"(ENABLE_REAL_NETWORK_KILL=False). Komutlar sadece loglanacak.{Style.RESET_ALL}")
        logging.info("SİMÜLASYON MODU: Ağ izolasyonu tetiklendi fakat gerçek komut çalıştırılmadı.")
        return

    try:
        if system == "nt":
            print(f"{Fore.CYAN}[*] Windows tespit edildi. Ağ adaptörleri devre dışı bırakılıyor...{Style.RESET_ALL}")
            subprocess.run(["ipconfig", "/release"], shell=True,
                            capture_output=True, timeout=15)
            result = subprocess.run(
                ["netsh", "interface", "show", "interface"],
                shell=True, capture_output=True, text=True, timeout=15
            )
            logging.info(f"Mevcut arayüzler:\n{result.stdout}")

            for line in result.stdout.splitlines():
                parts = line.split()
                if len(parts) >= 4 and parts[0] in ("Enabled", "Etkin"):
                    iface_name = " ".join(parts[3:])
                    subprocess.run(
                        ["netsh", "interface", "set", "interface", iface_name, "admin=disable"],
                        shell=True, capture_output=True, timeout=15
                    )
                    logging.info(f"Arayüz devre dışı bırakıldı: {iface_name}")

        elif system == "posix":
            print(f"{Fore.CYAN}[*] Linux/Unix tespit edildi. Ağ arayüzleri kapatılıyor...{Style.RESET_ALL}")
            result = subprocess.run(
                ["ip", "-o", "link", "show"],
                capture_output=True, text=True, timeout=15
            )
            logging.info(f"Mevcut arayüzler:\n{result.stdout}")

            for line in result.stdout.splitlines():
                iface = line.split(":")[1].strip().split("@")[0]
                if iface and iface != "lo":
                    subprocess.run(
                        ["sudo", "ip", "link", "set", iface, "down"],
                        capture_output=True, timeout=15
                    )
                    logging.info(f"Arayüz kapatıldı: {iface}")
        else:
            print(f"{Fore.RED}[!] Desteklenmeyen işletim sistemi: {system}{Style.RESET_ALL}")
            logging.error(f"Desteklenmeyen OS için izolasyon denemesi: {system}")

        print(f"{Fore.GREEN}[✓] Ağ izolasyon komutları çalıştırıldı.{Style.RESET_ALL}")
        logging.info("Ağ izolasyon prosedürü tamamlandı.")

    except Exception as e:
        print(f"{Fore.RED}[HATA] Ağ izolasyonu sırasında hata: {e}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[İPUCU] Bu işlem genelde yönetici/root yetkisi gerektirir.{Style.RESET_ALL}")
        logging.error(f"Ağ izolasyon hatası: {e}")


class CanaryHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.triggered = False  

    def _trigger(self, reason: str):
        if self.triggered:
            return  
        self.triggered = True
        print_alarm(reason)
        isolate_network()

    def on_modified(self, event):
        if event.is_directory:
            return
        self._trigger(f"Dosya değiştirildi (olası şifreleme): {event.src_path}")

    def on_deleted(self, event):
        if event.is_directory:
            return
        self._trigger(f"Dosya silindi (olası temizlik/wipe davranışı): {event.src_path}")

    def on_moved(self, event):
        dest = getattr(event, "dest_path", "")
        _, ext = os.path.splitext(dest)
        ext = ext.lower()

        if ext in SUSPICIOUS_EXTENSIONS:
            self._trigger(
                f"ŞÜPHELİ UZANTI TESPİT EDİLDİ! '{event.src_path}' -> '{dest}' "
                f"(uzantı: {ext})"
            )
        else:
            self._trigger(f"Dosya yeniden adlandırıldı/taşındı: {event.src_path} -> {dest}")

    def on_created(self, event):
        if event.is_directory:
            return
        _, ext = os.path.splitext(event.src_path)
        if ext.lower() in SUSPICIOUS_EXTENSIONS:
            self._trigger(
                f"ŞÜPHELİ YENİ DOSYA OLUŞTURULDU: {event.src_path} (uzantı: {ext})"
            )


def main():
    banner()
    ensure_canary_dir()

    event_handler = CanaryHandler()
    observer = Observer()
    observer.schedule(event_handler, path=CANARY_DIR, recursive=True)
    observer.start()

    print(f"{Fore.GREEN}[+] Zerguz izleme moduna geçti. Tuzak klasör dinleniyor...{Style.RESET_ALL}")
    print(f"{Fore.CYAN}    Çıkmak için CTRL+C basın.{Style.RESET_ALL}\n")
    logging.info("Zerguz başlatıldı, izleme başladı.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print(f"\n{Fore.YELLOW}[!] Zerguz kapatılıyor...{Style.RESET_ALL}")
        logging.info("Zerguz kullanıcı tarafından durduruldu.")
    observer.join()


if __name__ == "__main__":
    main()
