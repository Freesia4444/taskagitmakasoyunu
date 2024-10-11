# bu kod Duygu Cakir  adlı youtube kanalındaki "16 Python ile Hileli Taş Kağıt Makas Oyunu" dan öğrenme amaçlı yazıldı.
import random
def bilgisayar():
    n = random.randint(1,3)
    if n==1 :
        return "taş"
    elif n==2 :
        return "makas"
    else:
        return "kağıt"
while True:
 kullanici = input("taş, kağıt, makas ?")
 secim= bilgisayar()
 print("Bilgisayar :", secim)

 if secim == kullanici :
    print("berabere")
 elif secim == "kağıt" and kullanici == "makas":
    print("kazandın.")
 elif secim == "makas" and kullanici == "taş":
    print("kazandın.")
 elif secim == "makas" and kullanici == "taş":
    print("kazandın")
 else :
    print("Kaybettin!!!")