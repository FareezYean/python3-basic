#looping = pengulangan
jumlahrentang = 5 
for item in range(jumlahrentang):
    print ("BANGKEK LU: ", item)

kataKu = "BANGKEK"
for huruf in kataKu:
   print (huruf)

#item (variabel baru) adalah index
#range (jumlah rentang) adalah targetnya
#huruf (variabel baru) adalah index
#kataKu adalah targetnya

#perulangan while (sampai terpenuhi / true)
jawab = "ya"
hitung = 0
#selama inout dari variabel jawab
#diisi "ya" maka akan diulangi terus
while(jawab == "ya"):
    jawab = input("Lagi gak ni!! ")
    hitung += 1

print ("program diulangi sebanyak")