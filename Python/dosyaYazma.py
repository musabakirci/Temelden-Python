with open(r"C:\Users\MUSA\Desktop\Python tekrar\Tekrar\dosya.txt", "w", encoding="utf-8") as file:

    file.write("SİVAS CUMHURİYET ÜNİVERSİTESİ BİLGİSAYAR MÜHENDİSLİĞİ\n")   
    file.write("AQUATECH TEKNOFEST TAKIMI\n")

with open(r"C:\Users\MUSA\Desktop\Python tekrar\Tekrar\dosya.txt", "r", encoding="utf-8") as file:
    for i in file:
        print(i, end="")

 