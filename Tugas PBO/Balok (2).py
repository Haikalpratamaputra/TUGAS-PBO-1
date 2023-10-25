# Menghitung luas dan Volume balok

# Atur nilai variabel
print("Masukan Nilai")
p = float(input("Panjang: "))
l = float(input("Lebar: "))
t = float(input("Tinggi: "))

# Rumus
luas_permukaan = (2 * p * l ) + (2 * p * t) + (2 * l * t)
volume = p * l * t

# Output
print("hasil perhitungan")
print("luas permukaan balok: ", luas_permukaan)
print("volume: ", volume)