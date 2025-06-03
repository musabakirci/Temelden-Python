# Not Uygulaması

# 1- Menu   
     # 1- Not Ekle
     # 2- Ortalamaları Göster (90-100 -> AA, 80-89 -> BA) 
     # 3- Notları Kayıt Et
     # 4- Çıkış

def not_ekle():
    ad = input("Öğrenci Adi: ")
    soyad = input("Öğrenci Soyadi: ")
    not1 = int(input("1. Not: "))
    not2 = int(input("2. Not: "))
    not3 = int(input("3. Not: "))

    with open(r"C:\Users\MUSA\Desktop\Python tekrar\Tekrar\sinavNotlari.txt", "a", encoding="utf-8") as file:
        file.write(ad + " " + soyad + ":" + str(not1) + "," + str(not2) + "," + str(not3) + "\n")



def notlari_oku():
    with open(r"C:\Users\MUSA\Desktop\Python tekrar\Tekrar\sinavNotlari.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(satir)
def notlari_kayit_et():
    pass

while True:
    islem = input("1- Not Ekle\n2- Notlari Oku\n3- Notlari Kayit Et\n4- Çikiş\nSeçiminiz: ")

    if islem == "1":
        not_ekle()
    elif islem == "2":
        notlari_oku()
    elif islem == "3":
        notlari_kayit_et()
    else:
        break