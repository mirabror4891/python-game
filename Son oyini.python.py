"""Son o'yini"""

import random as r
def sontop(x=10):
    son=r.randint(1,x)
    print("Men 1 dan ", x, "gacha son oyladim topishga xarakat qling: ")
    taxminlar=0
    while True:
        taxminlar +=1
        javob=int(input(">>>"))
        if son>javob:
            print("Men oylagan son sizning javobingizdan kattaroq")
        elif son<javob:
            print("Men o'ylagan son sizning javobingizdan kichikroq")
        elif son==javob:
            break
       
    print(f"Tabriklaymiz, siz {taxminlar} ta taxminda topdingiz ")
    return taxminlar 

def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = r.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
                      f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim!")
    return taxminlar

def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        
        if taxminlar_user>taxminlar_pc:
            print(f"Men {taxminlar_pc} taxmin bilan topdim va  yutdim!")
        elif taxminlar_user<taxminlar_pc:
            print(f"Siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0):"))
print(play())
