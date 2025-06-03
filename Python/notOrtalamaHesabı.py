""" Bir öğrencinin 2 yazili bir sözlü notunu alarak ortalamasini hesaplayan ve hesaplanan ortalamaya göre not
araliğina karşilik gelendeğerlendirmeyi yapan bir Python programi"""
"""
0-24 : 0
25-44 : 1
45-54 : 2
55-69 : 3
70-84 : 4
85-100 : 5
"""
not1 = float(input("1. yazili notu: "))
not2 = float(input("2. yazili notu: "))
sozlu = float(input("Sözlü notu: "))
ortalama = (not1 + not2 + sozlu) / 3
if ortalama >= 0 and ortalama <= 24:
    print("Not araliği: 0")     
elif ortalama >= 25 and ortalama <= 44:
    print("Not araliği: 1") 
elif ortalama >= 45 and ortalama <= 54:
    print("Not araliği: 2")
elif ortalama >= 55 and ortalama <= 69:
    print("Not araliği: 3")
elif ortalama >= 70 and ortalama <= 84:
    print("Not araliği: 4")
elif ortalama >= 85 and ortalama <= 100:
    print("Not araliği: 5")
else:
    print("Yanliş not araliği girdiniz.")
print("Ortalama: ", ortalama)