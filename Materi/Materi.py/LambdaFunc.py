# lambda args : expression

# def = fungsi lebih dari 1 baris
def HalloKak (Nama) :
    print (f"Hallo Kak {Nama}")
    print (f"apa kabar kak {Nama} ?")

# f = format string gunakan { } untuk variable

# lambda = fungsi anonim yang 1 baris saja
HalloDek = lambda Nama : print(f"Hallo Dek {Nama}")
# fungsi tidak berguna jika gak dipanggil

HalloKak("Rafif")
HalloDek("Faye")

# https://youtu.be/xWdHduL8vVQ?feature=shared

# higher order function (map, sorted, fiter)
UangTF = [150.000, 200.000, 100.000]
print(f"Uang TF: {UangTF}")

# map = mentransformasi data item
KurangTF = map(lambda Uang : Uang - 50.000, UangTF)
listKurangTF = list(KurangTF)
print(f"Uang TF setelah dipotong 50.000: {listKurangTF}")

# sorted = mengurutkan data
UrutkanUang = sorted(UangTF)
BalikUang = sorted(UangTF, reverse=True)
print(f"Uang TF diurutkan: {UrutkanUang}")
print(f"Uang TF diurutkan terbalik: {BalikUang}")

# filter = menyaring data item sesuai kondisi
SaringUang = filter(lambda Uang : Uang > 150.000, UangTF)
listSaringUang = list(SaringUang)
print(f"Uang TF yang lebih besar: {listSaringUang}")