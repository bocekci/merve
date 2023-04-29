# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 23:58:21 2023

@author: Merve
"""

import random

def pc_secimi_uret():
    n = random.randint(1, 3)
    if n == 1:
        return "taş"
    elif n == 2:
        return "kağıt" 
    else:
        return "makas"

def hileli_pc_secimi_uret(kullanici_secimi):
    if kullanici_secimi == "taş":
        return "kağıt"
    elif kullanici_secimi == "kağıt":
        return "makas"
    else:
        return "taş"

skor_kullanici = 0
skor_pc = 0

while True:
    kullanici_secimi = input("taş, kağıt, makas seçin (çıkmak için q): ")
    
    if kullanici_secimi == "q":
        break
    
    # pc_secimi = pc_secimi_uret()
    pc_secimi = hileli_pc_secimi_uret(kullanici_secimi)
    print("Bilgisayarın seçimi:", pc_secimi)
    
    if pc_secimi == kullanici_secimi:
        print("Berabere kaldınız")
    elif pc_secimi == "taş" and kullanici_secimi == "kağıt":
        skor_kullanici += 1
        print("Kullanıcı kazandı!")
    elif pc_secimi == "kağıt" and kullanici_secimi == "makas":
        skor_kullanici += 1
        print("Kullanıcı kazandı!")
    elif pc_secimi == "makas" and kullanici_secimi == "taş":
        skor_kullanici += 1
        print("Kullanıcı kazandı!")
    else:
        skor_pc += 1
        print("Bilgisayar kazandı!")
    
    print("Siz:", skor_kullanici, "VS PC:", skor_pc)
    if skor_kullanici == 3 or skor_pc == 3:
        break

if skor_kullanici > skor_pc:
    print("Kazandınız! :)")
else:
    print("Kaybettiniz! :(")
