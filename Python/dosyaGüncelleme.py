# with open(r"C:\Users\MUSA\Desktop\Python tekrar\Tekrar\markalar.txt","a") as file:
#     file.write("\n")
#     file.write("6-Mercedes")

with open(r"C:\Users\MUSA\Desktop\Python tekrar\Tekrar\markalar.txt","r+",encoding="utf-8") as file:
    file.seek(0)
    file.write("1-Ford")
    
with open(r"C:\Users\MUSA\Desktop\Python tekrar\Tekrar\markalar.txt","r") as file:
    print(file.read())