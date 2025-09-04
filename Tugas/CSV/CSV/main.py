import csv 

# Baca semua data dari csv

with open("Keuangan.csv",newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)
print(data)

# 1. Tampilkan semua data

print("📌 Semua data :")
for row in data:
    print (f"{row['Tanggal']} | {row['Keterangan']} | {row['Kategori']} | {row['Jumlah']}")

# 2. Hitung pengeluaran

total = sum(int(row['Jumlah'])for row in data)
print (f"Total pengeluaran : Rp{total}")