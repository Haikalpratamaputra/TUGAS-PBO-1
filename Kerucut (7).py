# Menghitung luas perrmukaan kerucut dan volume

# Atur nilai variabel
print("masukan nilai")
phi = 3.14
r = float(input("Jari - jari: "))
s = float(input("Garis Pelukis: "))
t = float(input("Tinggi: "))
print("phi:", phi)

# Rumus
luas_permukaan = (phi * r * s) + (phi * r**2)
luas_selimut = phi * r * s
volume = phi * r ** 2 * t / 3

# Output
print("hasil perhitungan")
print("luas permukaan kerucut: ", luas_permukaan)
print("luas selimut: ", luas_selimut)
print("volume: ", volume)