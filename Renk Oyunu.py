import random
while True:
    print("""
HANGİ RENGİ TUTTUM TAHMİN ET BAKALIM
""")
    try:
        renkler = ["mavi" , "sarı" , "yeşil" , "beyaz",]
        mavi = renkler[0]
        sarı = renkler[1]
        yeşil = renkler[2]
        beyaz = renkler[3]
        veri = input("""Bir Renk Giriniz; 
Renkler: mavi , yeşil , beyaz , sarı =""")
        pc = random.choice(renkler)
        if veri == pc:
            print("Tebrikler")
        else:
            print("Tekrar Deneyiniz...")
    except ValueError:
        print("Sadece Belirtilen Renkleri Giriniz...")
