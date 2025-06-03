# Bir aracın yakıt tipine göre (benzin, dizel, lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan bir Python programı
#  benzin : 39.35
#  dizel : 41.45
#  lpg : 11.75

benzinfiyat = 39.35
dizelfiyat = 41.45
lpgfiyat = 11.75

toplamYakitUcreti = 0
ortalamYakitTuketimi = float(input("Aracın ortalama yakıt tüketimi (L/100km) : "))
mesafe = float(input("Gidilecek mesafe (km) : "))
yakitTipi = input("Yakıt tipi (benzin, dizel, lpg) : ")

toplamYakitTuketimi = mesafe * ortalamYakitTuketimi / 100

if yakitTipi == "benzin":
    toplamYakitUcreti = (benzinfiyat * toplamYakitTuketimi)
elif yakitTipi == "dizel":
    toplamYakitUcreti = (dizelfiyat * toplamYakitTuketimi)
elif yakitTipi == "lpg":    
    toplamYakitUcreti = (lpgfiyat * toplamYakitTuketimi)
else:
    print("Yanliş yakit tipi girdiniz.")

if toplamYakitUcreti != 0: 
    print("Toplam yakit ücreti : ", toplamYakitUcreti)