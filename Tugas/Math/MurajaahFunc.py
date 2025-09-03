import PerTambahan
import Perkalian

# Function

def Sapa(Sapa):
   print("IRASHAIMASE")
   print(Sapa, "Sensei")

# Spawn function
Sapa("Hamka")
print("================")
Sapa("Daffa")
print("================")
Sapa("Andy")
print("================")


# Function menggunakan parameter

# Tambah tambahan
def Tambah(angka1, angka2):
   return angka1 + angka2

# Spawn function
print("Hasil Penjumlahan = ", Tambah(60, 40))

# Importing the PerTambahan module
print(PerTambahan.tambah(10, 20))

print(Perkalian.Kali(10, 20))



   
