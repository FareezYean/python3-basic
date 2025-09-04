import requests
print (" Belajar API ==MATERI TERAKHIR==")
print ("-" * 40)
url =" https://api.aladhan.com/v1/timingsByCity/28-08-2025?city=Jakarta&country=Indonesia&method=5 "
response = requests.get(url)    # HTTP GET
data_json = response.json()     # konversi ke JSON
jadwal_sholat = (data_json['data']['timings'])
tgl_hijri = data_json['data']['date']['hijri']['date']
print (f"tanggal hijriah : {tgl_hijri}")
print ("Jadwal Sholat :")
print (f"-> Shubuh : {jadwal_sholat['Fajr']}")
print (f"-> Maghrib : {jadwal_sholat['Maghrib']}")
