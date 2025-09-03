
# FILE HANDLING

# file extension yg membedakan file satu dengan lainnya, lihat diakhir nama file
# .py (pythone) , .doc (word), .txt (text), .jpg (image), .mp3 (audio)
# cari posisi file yg mau dibuka
file_path = r"C:\Users\Thinkpad T490\Desktop\Belajar PYTHON\Materi.py\FileHandling\Pesan.txt"
# buka file target dengan mode tertentu
file_pesan = open(file_path, "r") # read only
# fungsi read adalah membaca semua isi file
baca_pesan = file_pesan.read()
print (f"isi pesannnya: {baca_pesan}")
# tutup file
file_pesan.close()
# kalo masih bulet ketik ctrl + s