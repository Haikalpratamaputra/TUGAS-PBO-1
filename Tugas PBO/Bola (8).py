# Menghitung luas permukaan bola dan volume

# Atur nilai variabel
print("masukan nilai")
phi = 3.14
r = float(input("Jari - jari: "))
print("phi:", phi)

# Rumus
luas_permukaan = 4 * phi * r ** 2
volume = 4/3 * phi * r ** 3

# Output
print("hasil perhitungan")
print("luas permukaan bola: ", luas_permukaan)
print("volume: ", volume)