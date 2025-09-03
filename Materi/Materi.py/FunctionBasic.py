# buat fungsi dengan def lalu nama fungsi
# parameter nama untuk mengambil nilai dari luar ke isi fungsi
def HelloWorld(NAMA):
    print("KONNICHIWAA")
    print("Mr. ", NAMA)
    print("===============")

# print nama fungsi disertai (  )
HelloWorld("Saitama")
HelloWorld("Garou")
HelloWorld("Genos")

# fungsi luas persegi panjang
def LuasPersegiPanjang(Panjang, Lebar):
    print("P = ", Panjang)
    print("L = ", Lebar)
    Rumus = Panjang * Lebar
    print("Luas Persegi Panjang = ", Rumus)
LuasPersegiPanjang(10, 5)

# fungsi luas segitiga
def LuasSegitiga(Alas, tinggi):
    print("A = ", Alas)
    print("T = ", tinggi)
    Rumus = (Alas * tinggi) / 2
    print("Luas Segitiga = ", Rumus)
LuasSegitiga(10, 5)

# fungsi luas belah ketupat
def LuasBelahKetupat(D1, D2):
    print("D1 = ", D1)
    print("D2 = ", D2)
    Rumus = (D1 * D2) / 2
    print("Luas Belah Ketupat = ", Rumus)
LuasBelahKetupat(10, 5)

# fungsi luas keliling belah ketupat
def LuasKelilingBelahKetupat(Sisi1, sisi2):
    print("sisi1 = ", Sisi1)
    print("sisi2 = ", sisi2)
    Rumus = 2 * (Sisi1 + sisi2)
    print("Keliling Belah Ketupat = ", Rumus)
LuasKelilingBelahKetupat(10, 5)

print (" Rafif-san")

# fungsi keliling lingkaran
def KelilingLingkaran(jari):
    print("Jari-jari = ", jari)
    Rumus = 2 * 22/7 * jari
    print("Keliling Lingkaran = ", Rumus)
KelilingLingkaran(3)
print ("Rafif-san")
print ("lagi!!!")
    