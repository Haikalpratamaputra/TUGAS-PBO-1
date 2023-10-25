# Menghitung luas permukaan prisma segita dan volume

# Atur nilai variabel
print("masukan nilai")
S1 = float(input("Sisi 1: "))
S2 = float(input("Sisi 2: "))
S3 = float(input("Sisi 3: "))
T = float(input("Tinggi Prisma: "))
a = float(input("Alas: "))
t = float(input("Tinggi: "))

# Rumus
luas_selimut = (S1 + S2 + S3) * T
luas_permukaan = (S1 + S2 + S3) * T * a * t 
volume = a * t * T / 2 

# Output
print("hasil perhitungan")
print("luas selimut: ", luas_selimut)
print("luas permukaan prisma segitiga: ", luas_permukaan)
print("volume: ", volume)