#!/usr/bin/python
import hashlib
import os
os.system("clear")
def komut_var_mi(komut):
    # Komutun çıktısını almak için "which" komutunu kullan
    cikti = os.popen(f"which {komut}").read()

    # Çıktıda boşluk veya satır sonu karakteri yoksa, komut mevcuttur
    if cikti.strip() == "":
        return False
    else:
        return True

# figlet paketini kontrol et
if not komut_var_mi("figlet"):
    try:
        os.system("sudo apt install figlet")
    except:
        print("Komut çalıştırılırken bir hata oluştu.")

os.system("clear")
os.system("figlet Karambolock")
print("")
def sifrele(mesaj):
    sifreli_mesaj = ""
    shift = 3  # Shift value for the Caesar cipher
    for harf in mesaj:
        sifreli_harf = chr((ord(harf) - 32 + shift) % 95 + 32)
        sifreli_mesaj += sifreli_harf
    return sifreli_mesaj

def coz(sifreli_mesaj):
    mesaj = ""
    shift = 3  # Shift value for the Caesar cipher
    for harf in sifreli_mesaj:
        orijinal_harf = chr((ord(harf) - 32 - shift) % 95 + 32)  
        mesaj += orijinal_harf
    return mesaj


secenek = input("Şifrele (s) veya Çöz (ç) seçin: ")

if secenek == "s":
    mesaj = input("Şifrelemek istediğiniz mesajı girin: ")
    sifreli_mesaj = sifrele(mesaj)
    with open("sifreli_mesaj.txt", "w") as dosya:
        dosya.write(sifreli_mesaj)
        print("Mesaj şifrelenerek 'sifreli_mesaj.txt' dosyasına kaydedildi.")
elif secenek == "ç":
    sifreli_mesaj = input("Çözmek istediğiniz şifreli mesajı girin: ")
    mesaj = coz(sifreli_mesaj)
    with open("cozulmus_mesaj.txt", "w") as dosya:
        dosya.write(mesaj)
        print("Şifre çözülerek 'cozulmus_mesaj.txt' dosyasına kaydedildi.")
else:
    print("Geçersiz seçenek!")
