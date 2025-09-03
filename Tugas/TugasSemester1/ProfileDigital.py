# ====Chalengge Start====

NamaLengkap = input("Masukkan Nama Lengkap: ")
Umur = input("Masukkan Umur: ")
Kelas = input("Masukkan Kelas: ")
Cita = input("Masukkan Cita-Cita atau profesi impian: ")
Hobi = input("Masukkan Hobi: ")
Belajar = input("Lebih suka belajar pagi atau malam? ")

print("")

print("Pilih tipe gaya digital kamu (ketik angkanya aja):")
print("1. Wibu (Anak anime banget)")
print("2. Gamer (Ranked jalan terus)")
print("3. K-Popers (Ngikutin gaya Korea)")
print("4. Anak konten (Tiktoker/Youtuber wannabe)")
print("5. Anak nongki (Yang penting ngumpul)")

print("")

type = input("Masukkan pilihan kamu (1-5): ")

if type == "1":
    waifu = input("Siapa waifu atau husbando kamu? ")
    print("Waifu/Husbando kamu adalah:", waifu)
    komen1 = ("Kereenn, kamu suka anime!")
    print("Aku juga suka", waifu, "!")
elif type == "2":
    game = input("Game favorit kamu apa? ")
    print("Game favorit kamu adalah:", game)
    komen2 = ("Keren, kamu gamer sejati!")
    print("Aku juga main", game, "!")
elif type == "3":
    bias = input("Siapa bias kamu? ")
    print("Bias kamu adalah:", bias)
    komen3 = ("Keren, kamu K-Popers sejati!")
    print("Aku juga suka", bias, "!")
elif type == "4":
    platform = input("Platform favorit kamu? TikTok? YouTube? ")
    print("Platform favorit kamu adalah:", platform)
    komen4 = ("Keren, kamu anak konten!")
    print("Aku juga suka nonton di", platform, "!")
elif type == "5":
    tempat = input("Nongkrong paling sering di mana? ")
    print("Tempat nongkrong favorit kamu:", tempat)
    komen5 = ("Keren, kamu anak nongki sejati!")
    print("Aku juga suka nongkrong di", tempat, "!")
else:
    print("Pilihan tidak valid.")

print("")

ask = input("Apakah Teman Disebelah Kamu Bau: ")
if ask == "ya":
    komentar = "Wah, temanmu harus mandi lebih sering!"
elif ask == "tidak":
    komentar = "Wah, temanmu pasti rajin mandi!"
print("")

print("===========================")
print ("=== Profil Digital Kamu ===")
print ("Nama Lengkap:", NamaLengkap)
print ("Umur:", Umur)
print ("Kelas:", Kelas)
print ("Cita-Cita:", Cita)
print ("Hobi:", Hobi)
print ("Waktu Belajar Paling Enak:", Belajar)
tgl = 2025 - int(Umur)
print ("Tahun lahir:", tgl)

print("")

print("=== Tipe Digital Kamu ===")
print("Tipe:", type)
if type == "1":
    print("Waifu/Husbando:", waifu)
    print("Komen:", komen1)
elif type == "2":
    print("Game favorit:", game)
    print("Komen:", komen2)
elif type == "3":
    print("Bias:", bias)
    print("Komen:", komen3)
elif type == "4":
    print("Platform favorit:", platform)
    print("Komen:", komen4)
elif type == "5":
    print("Tempat nongkrong:", tempat)
    print("Komen:", komen5)

print("")

print ("Teman Sebelah Kamu Bau ???", ask)
print("Komentar:", komentar)
print("===========================")

