#!/usr/bin/python
import hashlib
import os
os.system("clear")
def komut_var_mi(komut):
    cikti = os.popen(f"which {komut}").read()
    if cikti.strip() == "":
        return False
    else:
        return True
if not komut_var_mi("figlet"):
    try:
        os.system("sudo apt install figlet")
    except:
        print("An error occurred while executing the command.")

os.system("clear")
os.system("figlet Karambolock")
print("")
def sifrele(mesaj):
    sifreli_mesaj = ""
    shift = 3  
    for harf in mesaj:
        sifreli_harf = chr((ord(harf) - 32 + shift) % 95 + 32)
        sifreli_mesaj += sifreli_harf
    return sifreli_mesaj

def coz(sifreli_mesaj):
    mesaj = ""
    shift = 3  
    for harf in sifreli_mesaj:
        orijinal_harf = chr((ord(harf) - 32 - shift) % 95 + 32)  
        mesaj += orijinal_harf
    return mesaj


secenek = input("Select Encrypt (e) or Decrypt (d): ")

if secenek == "e":
    mesaj = input("Enter the message you want to encrypt: ")
    sifreli_mesaj = sifrele(mesaj)
    with open("encrypted-message.txt", "w") as dosya:
        dosya.write(sifreli_mesaj)
        print("The message was encrypted and saved in the file 'encrypted-message.txt' ")
elif secenek == "d":
    sifreli_mesaj = input("Enter the encrypted message you want to decrypt: ")
    mesaj = coz(sifreli_mesaj)
    with open("decrypted.txt", "w") as dosya:
        dosya.write(mesaj)
        print("The password was decrypted and saved in the file 'decrypted.txt'")
else:
    print("Invalid option!")
