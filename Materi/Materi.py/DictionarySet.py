print  ("SET")

# set = {} = tidak berurutan , berubah , tidak boleh duplikat
game_rafif = {"Genshin Impact", "Mobile Legends", "Free Fire", "roblox"}
game_faye = {"blood strike", "Free Fire", "minecraft", "roblox"}

# .add = () = menambah item ke set
game_rafif.add("PUBG Mobile")
game_faye.add("Call of Duty")

# .remove = () = menghapus item dari set
game_rafif.remove("Free Fire")
game_faye.remove("minecraft")

# len = () = menghitung jumlah item dalam set
print("Jumlah game Rafif:", len(game_rafif))
print("Jumlah game Faye:", len(game_faye))

# union = () = menggabungkan dua set
gabungan_game = game_rafif.union(game_faye)
print("Gabungan game Rafif dan Faye:", gabungan_game)

# intersection = () = mencari item kembar di kedua set berbeda
game_kembar = game_rafif.intersection(game_faye)
print("Game yang sama di Rafif dan Faye:", game_kembar)

# difference = () = mencari item yang berbeda di kedua set berbeda
game_beda = game_rafif.difference(game_faye)
print("Game Rafif yang tidak ada di Faye:", game_beda)

print  ("DICT")

# dict (dictionary) = { key : value }  / { kunci : isinya } 
# berurutan berdasarkan key, berubah, key tidak boleh duplikat

Daftar_Anime = {
    "ONE_PUNCH_MAN" : "Saitama",
    "DEMON_SLAYER" : "Tanjiro Kamado",
    "ATTACK_ON_TITAN" : "Eren Yeager",
    "WAIFU" : {
      "SPY_X_FAMILY" : "ANYA FORGER",
      "AHAREN_SAN_WA_HAKARENAI" : "AHAREN_SAN",
      "KOE_NO_KATACHI" : "NISHIMIYA SHOUKO"
     }
}

print ("Daftar Anime:", Daftar_Anime)
print ("Waifu:", Daftar_Anime["WAIFU"] ["SPY_X_FAMILY"])
print ("Idola:", Daftar_Anime["ONE_PUNCH_MAN"])
