# Menghitung luas permukaan dan volume Limas Segitiga

# Atur nilai variabel
print("masukan nilai")
LS1 = float(input("Luas Segitiga 1: "))
LS2 = float(input("Luas Segitiga 2: "))
LS3 = float(input("Luas Segitiga 3: "))
LS4 = float(input("Luas Segitiga 4: "))
a = float(input("Luas Alas: "))
t = float(input("Tinggi: "))
T = float(input("Tinggi Limas: "))

# Rumus
luas_permukaan = LS1 + LS2 + LS3 + LS4
volume = a * T * t / 6

# output
print("hasil perhitungan")
print("luas permukaan limas segitiga: ", luas_permukaan)
print("volume: ", volume)