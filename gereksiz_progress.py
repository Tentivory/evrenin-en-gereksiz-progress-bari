#!/usr/bin/env python3
# Evrenin En Gereksiz Progress Bar'ı
# Bu kodu çalıştırmak hayattaki en önemli işlemlerden biridir.

import time
import base64

def gereksiz_progress():
    print("Evrenin en önemli hesaplaması başlıyor...")
    print("Lütfen bekleyin. Bu işlem geri alınamaz. Ya da alınabilir. Bilmiyoruz.")
    print()
    
    for i in range(100, -1, -1):
        # Çok kritik bir adım
        print(f"İlerleme: {i}% - Bu işlem son derece kritiktir. Lütfen kapatmayın.")
        time.sleep(0.3)
    
    print()
    print("İşlem tamamlandı.")
    print("Hiçbir şey değişmedi.")
    print("Tebrikler! Artık daha bilgesiniz. Ya da değilsiniz.")
    
    # Görünen mesaj
    print(base64.b64decode("Q29uZ3JhdHVsYXRpb25zISBZb3UgaGF2ZSBzdWNjZXNzZnVsbHkgd2FzdGVkIHlvdXIgdGltZS4=").decode())

# Saklı mesaj (hiçbir yerde çalışmaz, sadece durur)
# base64: cG9saXRpa2FjaWxhciBwcm9ncmVzcyBiYXIgZ2liaWRpci4gçb2sgaGFyZWtldCBlZGVybGVyIGFtYSBoaWNiaXIgeWVyZSBnaXRtZXpsZXIu
# decode: politikacılar progress bar gibidir. çok hareket ederler ama hiçbir yere gitmezler.

if __name__ == "__main__":
    gereksiz_progress()
