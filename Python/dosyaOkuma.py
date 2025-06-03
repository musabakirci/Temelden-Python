"""
    Dosya  açmak ve oluşturmak için open() fonksiyonu kullanilir.

    Dosya açma modlari:
    Kullanimi   : open(dosya_adi, dosya_erişme_modu)
    dosya_erişme_modu: Dosya açma modunu belirtir. Aşağidaki modlar kullanilabilir:
    r: Dosyayi okuma modunda açar. Dosya mevcut olmalidir.
    w: Dosyayi yazma modunda açar. Dosya mevcut değilse oluşturur, mevcutsa içeriğini siler.
    a: Dosyayi ekleme modunda açar. Dosya mevcut değilse oluşturur, mevcutsa içeriğini silmeden ekleme yapar.
    x: Dosyayi oluşturma modunda açar. Dosya mevcutsa hata verir.
    b: İkili modda açar. Dosya ikili veri içeriyorsa kullanilir.
    t: Metin modunda açar. Varsayilan moddur.
    r+: Dosyayi okuma ve yazma modunda açar. Dosya mevcut olmalidir.
    w+: Dosyayi okuma ve yazma modunda açar. Dosya mevcut değilse oluşturur, mevcutsa içeriğini siler.
    seek(): Dosya konumunu ayarlar. Dosya konumu, dosyanin başindan itibaren kaç byte okunduğunu belirtir.
"""

f = open(r"C:\Users\MUSA\Desktop\Python tekrar\Tekrar\log.txt", encoding="utf-8")  

print(f.read())  # Dosyanin içeriğini okur ve ekrana yazdirir.
f.close()  # Dosyayi kapatir.

# with'de file.close() fonksiyonu otomatik olarak çağrılır.
with open(r"C:\Users\MUSA\Desktop\Python tekrar\Tekrar\log.txt", encoding="utf-8") as f:
    print(f.read(10))  # Dosyanin içeriğini okur ve ekrana yazdirir.
    print(f.tell()) # Dosya konumunu gösterir.
    print(f.read())    
    print(f.tell()) 

try:
    with open(r"C:\Users\MUSA\Desktop\Python tekrar\Tekrar\log.txt", encoding="utf-8") as file:
        for i in file:
            print(i, end="")
except FileNotFoundError as e:
    print("Dosya bulunamadi:", e)