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