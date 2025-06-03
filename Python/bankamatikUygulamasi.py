#Bankamatik Uygulaması
# Kullanıcıdan hesap bilgilerini al
# menu, paraCekme, bakiyeSorgulama, paraYatirma fonksiyonları tanımlanacak
# Çekilmek istenen tutar hesapta yoksa ek hesabın kullanılmak istendiği sorulacak

hesaplar = [
    {
        "Ad": "Ali Yilmaz",
        "HesapNo": "1234567890",
        "Bakiye": 1000,
        "EkHesap": 500,
        "Sifre": "1234",
        "kullanniciAdi": "aliYilmaz",
    },
    {
        "Ad": "Ayse Demir",
        "HesapNo": "0987654321",
        "Bakiye": 2000,
        "EkHesap": 1000,
        "Sifre": "5678",
        "kullanniciAdi": "ayseDemir",
    },
    {
        "Ad": "Mehmet Can",
        "HesapNo": "1122334455",
        "Bakiye": 1500,
        "EkHesap": 750,
        "Sifre": "91011",
        "kullanniciAdi": "mehmetCan",
    },
]

# ... hesaplar tanımlı (aynı kalacak)

def paraYatirma(hesap):
    miktar = float(input("Yatırmak istediğiniz tutarı girin: "))
    if miktar > 0:
        hesap["Bakiye"] += miktar
        print(f"{miktar} TL başarıyla yatırıldı. Güncel bakiye: {hesap['Bakiye']} TL")
    else:
        print("Geçersiz miktar!")

def bakiyeSorgulama(hesap):
    print(f"Bakiyeniz: {hesap['Bakiye']} TL")
    print(f"Ek Hesap Bakiyeniz: {hesap['EkHesap']} TL")

def paraCekme(hesap):
    miktar = float(input("Çekmek istediğiniz tutarı girin: "))

    if hesap["Bakiye"] >= miktar:
        hesap["Bakiye"] -= miktar
        print(f"{miktar} TL başarıyla çekildi.")
    
    else:
        toplam = hesap["Bakiye"] + hesap["EkHesap"]

        if toplam >= miktar:
            ek_hesap_kullanimi = input("Ek hesabınızı kullanmak ister misiniz? (E/H): ").upper()

            if ek_hesap_kullanimi == "E":
                ek_hesap_miktar = miktar - hesap["Bakiye"]
                hesap["EkHesap"] -= ek_hesap_miktar
                hesap["Bakiye"] = 0
                print(f"{miktar} TL başarıyla çekildi. Ek hesabınızdan {ek_hesap_miktar} TL kullanıldı.")
            else:
                print("Yetersiz bakiye! İşlem iptal edildi.")
        else:
            print("Yetersiz bakiye! İşlem iptal edildi.")

def menu(hesap):
    while True:
        print("\n")
        print(f"Merhaba, {hesap['Ad']}")
        print("1. Para Çekme")
        print("2. Para Yatırma")
        print("3. Bakiye Sorgulama")
        print("4. Çıkış")
        
        try:
            secim = int(input("Seçiminizi yapın (1-4): "))
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
            continue

        if secim == 1:
            paraCekme(hesap)
        elif secim == 2:
            paraYatirma(hesap)
        elif secim == 3:
            bakiyeSorgulama(hesap)
        elif secim == 4:
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")

def login():
    while True:
        kullanici_adi = input("Kullanıcı adınızı girin: ")
        sifre = input("Şifrenizi girin: ")

        for hesap in hesaplar:
            if hesap["kullanniciAdi"] == kullanici_adi and hesap["Sifre"] == sifre:
                print("Giriş başarılı!")
                menu(hesap)
                return
        print("Kullanıcı adı veya şifre hatalı! Lütfen tekrar deneyin.")

# Program başlatılıyor
login()
