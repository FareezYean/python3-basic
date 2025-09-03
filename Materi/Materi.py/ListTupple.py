#Materi 6

#list = [ ]berurutan , berubah, boleh duplikat
daftar_belanja = ["pisang kembung", "gabin", "teh desa", "tahu golek", 5000]
print ("tas belanja:", daftar_belanja)
#akses item dgn index
print (daftar_belanja [2])

game_favorit = ["Genshin Impact",
                 "PUBG Mobile",
                   "Free Fire"]
print ("Game favorit:", game_favorit)
print ("Game favorit ke-2:", game_favorit[1])

#===========================================================================

# Append () untuk menambah item ke akhir list
daftar_belanja.append ("tahu")
# Insert () untuk menambah item ke index tertentu
daftar_belanja.insert (1, "batagor")
print ("tas skrg", daftar_belanja)
# Remove () untuk hapus item
daftar_belanja.remove("teh desa")
print ("tas", daftar_belanja)
# Menggabungkan list +
jajanan_gw = ["gorengan", "teh desa"]
jajanan_lu = ["mixue", "janji jiwa"]
titip_jajan = jajanan_gw + jajanan_lu
print ("titipan", titip_jajan)
# Menggandakan item dengan *
print ("bilal nambah lagi", jajanan_lu* 3)
# List beracabang (list multi dimensi)
list_siswa = [
    ["Rafif", "10C", "Gamer"],
    ["Aisyah", "10B", "Wibu"],
    ["Budi", "10A", "Gamer"]
    ]
print ("list siswa:", list_siswa)
print (list_siswa [1] [2])

#==============================================================
# Tupple = ( ) tidak berurutan, tidak berubah, boleh duplikat
ttl = ("Jakarta", 1, "Januari", 2010)
print ("TTL:", ttl)
print ("bulan lahir rapip", ttl [2])
# Unpacking variabel
tempat_lahir, tgl_lahir, bln_lahir, thn_lahir = ttl
print ("bulan lahir:", bln_lahir)

# List
List_Hp = ["samsung", "iphone", "infinix", "vivo", "realme"]
print("Daftar HP:", List_Hp)

for item in List_Hp:
    print(item)

# Operasi dasar pada list

# Append
List_Hp.append("xiaomi")
print("Setelah append:", List_Hp)

# Insert
List_Hp.insert(5, "redmi")
print ("setelah insert:", List_Hp)

# Menghapus item

# Remove
List_Hp.remove("iphone")
print("Setelah remove:", List_Hp)

# Pop
List_Hp.pop(4)
print("Setelah pop:", List_Hp)

# Mengakses elemen list
print("hp gw", List_Hp[2])

# buat sebuah program yang
# 1. meminta user masukin 5 nama buah, satu per satu
# 2. nama nama buah tadi yg sudah dimasukkan oleh user, disimpan dgn append
# 3. tampilkan semua nama buah yg sudah dimasukkan

# contoh output

# daftar nama buah kamu
# 1, mangga
# 2, jeruk
# 3, apel
# 4, pisang
# 5, durian

buah_list = []

buah1 = input("Masukkan nama buah 1: ")
buah2 = input("Masukkan nama buah 2: ")
buah3 = input("Masukkan nama buah 3: ")
buah4 = input("Masukkan nama buah 4: ")
buah5 = input("Masukkan nama buah 5: ")

buah_list.append(buah1)
buah_list.append(buah2) 
buah_list.append(buah3)
buah_list.append(buah4)
buah_list.append(buah5)

for item in buah_list:
    print(item)