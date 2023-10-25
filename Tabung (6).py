# Menghitung luas permukaan tabung dan volume

# Atur nilai varibel
print("masukan nilai")
phi = 3.14
r = float(input("Jari - Jari: "))
t = float(input("Tinggi: "))
print("phi: ", phi)

# Rumus
luas_permukaan = (2 * phi * r * t) + (2 * phi * r ** 2)  
luas_selimut = 2 * phi * r * t
volume = phi * r ** 2 * t

# Output
print("hasil perhitungan")
print("luas permukaan tabung: ", luas_permukaan)
print("luas permukaan tabung: ", luas_selimut)
print("volume: ", volume)