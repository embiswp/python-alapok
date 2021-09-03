# Buborékrendezés
# 3 2 4 1
# 2 3 4 1
# 2 3 4 1
# 2 3 1 4
# 2 3 1 4
# 2 1 3 4
# 1 2 3 4

# 1. feladat: rakja sorba a program ezt: 3 2 4 1, írja ki a sorrendezés végén a listát
# 2. feladat: kérjen be egy tetszőleges számsort és azt sorrendezze

szamok = [30, 32, 24, 13, 41, 12, 52, 87, 14, 75, 34, 19]
for j in range(len(szamok)-1):
    for i in range(len(szamok)-j-1):
        if szamok[i] > szamok[i+1]:
            temp = szamok[i+1]
            szamok[i+1] = szamok[i]
            szamok[i] = temp
print(szamok)

# 3. feladat: cseréld meg két változó értékét
#ehhez a két sorhoz nem nyúlhatsz
# fiok1 = "alma"
# fiok2 = "narancs"

# atmenetifiok = fiok1
# fiok1 = fiok2
# fiok2 = atmenetifiok

# #ehhez a két sorhoz nem nyúlhatsz
# print(fiok1)
# print(fiok2)

#a legvégén azt lássuk hogy
#narancs
#alma
