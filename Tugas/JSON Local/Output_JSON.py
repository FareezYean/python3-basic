import json

with open('Peminjaman_Buku.json', newline="", encoding='utf-8') as f:
    data = json.load(f)

TotalPinjam = 0
TotalBelumKembali = 0
BelumKembali_List = []

for anggota in data['anggota']:
    nama = anggota['nama']
    for pinjam in anggota['pinjam']:
        TotalPinjam += 1
        if not pinjam['kembali']:
            TotalBelumKembali += 1
            BelumKembali_List.append(f"- {nama} : {pinjam['judul']} ({pinjam['tanggal']})")

print("Belum kembali:")
for item in BelumKembali_List:
    print(item)
print(f"\nTotal dipinjam: {TotalPinjam} | Belum kembali: {TotalBelumKembali}")