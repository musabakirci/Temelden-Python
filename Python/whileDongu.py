# 1- Başlangıç ve bitiş değerleri kullanıcıdan alınız ve bu değerler arasındaki tüm çift sayıları ekrana yazdırınız.   

baslangic = int(input("Başlangiç değeri: "))
bitis = int(input("Bitiş değeri: "))

i = baslangic
while i < bitis:
    if i % 2 == 0:
        print(i)
    i += 1


# 2- (1-100) arasındaki sayıları azalan şekilde yazdırınız.

i = 100
while i > 0:
    print(i)
    i -= 1


# 3- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazınız.

i = 0
sayilar = []

while i < 5:
    sayi = int(input("Sayi giriniz: "))
    sayilar.append(sayi)
    i += 1

sayilar.sort()
print(sayilar)

# Klavyeden girilen n sayıdaki öğrenci bilgisini liste içerisinde saklayınız.
# **4- Öğrenci bilgileri: ad, soyad, numara) şeklinde olsun.
#  **ürün ekleme işlemi bittiğinde öğrencileri listeleyiniz.

devammi = "e"
ogrenciler = []

while (devammi != "h"):
    ad = input("Öğrenci adi: ")
    soyad = input("Öğrenci soyadi: ")
    numara = input("Öğrenci numarasi: ")

    ogrenciler.append({
        "ad": ad,
        "soyad": soyad,
        "numara": numara
    })

    devammi = input("Devam etmek istiyor musunuz? (e/h): ")

for ogrenci in ogrenciler:
    print(f"{ogrenci['ad']} {ogrenci['soyad']} - {ogrenci['numara']}")    

# 5- 1-100 arasındaki çift sayıları sadece toplayan bir program yazınız.

i = 0
toplam = 0

while i <= 100:
    i += 1
    if i % 2 == 1:
        continue
    toplam += i

print("Toplam: ", toplam)
