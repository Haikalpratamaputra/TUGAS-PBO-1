# Menghitung luas permukaan limas segi empat dan volume

# Atur nilai variabel
print("masukan nilai")
LS1 = float(input("Luas Sisi 1: "))
LS2 = float(input("Luas Sisi 2: "))
LS3 = float(input("Luas Sisi 3: "))
LS4 = float(input("Luas Sisi 4: "))
LS5 = float(input("Luas Persegi: "))
La = float(input("Luas Alas: "))
T = float(input("Tinggi: "))

# Rumus
luas_permukaan = LS1 + LS2 + LS3 + LS4 + LS5
volume = La * T / 3

# Output
print("hasil perhitungan")
print("luas permukaan limas segi empat: ", luas_permukaan)
print("volume: ", volume)