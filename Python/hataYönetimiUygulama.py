liste = ["1","3","5","20b","abc","10a","60"]

# 1: Lİste elemanları içindeki sayısal değerleri bulunuz.

"""
for x in liste:
    try:
        sonuc = int(x)
        print(sonuc)
    except ValueError:
        continue
"""

# 2: Kullanıcı "quit (q)" değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz ksi halde hata mesajı yazın.    

"""
while True:
    sayi = input("Bir sayi giriniz (çikmak için 'q' yazin): ")
    if (sayi == "q"):
        break

    try:
        sonuc = float(sayi)
        print(f"Girdiğiniz sayi: ", sonuc)
        break
    except ValueError:
        print("Hata: Lütfen bir sayi giriniz.")
        continue
"""
# 3: Dictionary ve key bilgilerini parametre olarak alan get(dict, key) fonksiyonu yazınız.

urun = {"urunAdi":"Samsung S20", "fiyat":10000}

# d["fiyat"] => KeyError

# get(urun, "fiyat") => none
# get(urun, "urunAdi") => Samsung S20

def get(liste, key):
    try:
        return liste[key]
    
    except KeyError:
        print("Hata: Bu anahtar mevcut değil.")
        return None
    
sonuc = get(urun, "fiyat")
sonuc2 = get(urun, "urunAdi")
print(sonuc)