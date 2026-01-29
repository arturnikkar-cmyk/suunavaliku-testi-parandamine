# 1 meetod logi salvestamine
text = input("sisesta oma nimi ja rühmanimetus: ")
kuu = input("sisesta praegune kuupäev: ")
with open("TextFile1.txt", "a", encoding="utf-8") as file:
    file.write(text + kuu + "\n")
    print(text + " " + kuu)

# 2 meetod kalkulaator
print("Tavaline kalkulaator")
print("Vali tehe:")
print("+  liitmine")
print("-  lahutamine")
print("*  korrutamine")
print("/  jagamine")

op = input("Tehe: ")
a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))

if op == "+":
    print("Tulemus:", a + b)
elif op == "-":
    print("Tulemus:", a - b)
elif op == "*":
    print("Tulemus:", a * b)
elif op == "/":
    if b == 0:
        print("Viga: nulliga jagamine ei ole lubatud")
    else:
        print("Tulemus:", a / b)
else:
    print("Tundmatu tehe")

    import math #pythagorise teoreem

b = float(input("sisesta b: "))
c = float(input("sisesta c: "))
a = ( c - b )
print(a)
if a<0:
    print("VIGA!")

# 3 meetod kolmurg

a = int(input("Sisesta a: "))
b = int(input("Sisesta b: "))
c = int(input("Sisesta c: "))
ümbermõõt = a + b + c
print("Kolmnurga ümbermõõt:", ümbermõõt)




