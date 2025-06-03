# 1-Yas Hesaplama
def yasHesapla():
    return 2023 - int(input("Doğum yilinizi giriniz: "))
print("Yasiniz: ", yasHesapla())

# 2- Kendisine gönderilen bir kelimeyi belirtilen kez gösteren fonksiyonu yazınız

def yayzdir(test, adet):
    return test * adet

print(yayzdir("Cumhuriyet ", 5))

# 3- Dikdörtgenin alan ve çevresini hesaplayan bir fonksiyon yazınız
def dikdortgenHesapla(kisaKenar, uzunKenar):
    alan = kisaKenar * uzunKenar
    cevre = 2 * (kisaKenar + uzunKenar)

    return f"Alan: {alan} Cevre: {cevre}" 
sonuc =dikdortgenHesapla(10, 20)

# 4- Yazı tura uygulamısını fonksiyon kullanarak yapınız.
def yaziTura():
    import random
    sonuc = random.random()
    if sonuc > 0.5:
        return "Tura"
    else:
        return "Yazi"
    
Sonuc= yaziTura()

# 5- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.

def asalSayiBul(baslangic, bitis):
    for sayi in range(baslangic, bitis + 1):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i) == 0:
                    break
            else:
                print(sayi)

asalSayiBul(1, 100)
        
            