import requests
print ("==Al-Quran via API==")
print ("-" * 40)

# Ayat
url_ayat =" https://api.alquran.cloud/v1/ayah/2:255/quran-simple "
response_ayat = requests.get(url_ayat)    # HTTP GET
data_ayat = response_ayat.json()     # konversi ke JSON
ayat_arab = (data_ayat['data']['text'])

# Terjemah Bahasa Inggris
url_terjemah =" https://api.alquran.cloud/v1/ayah/2:255/en.asad "
response_terjemah = requests.get(url_terjemah)    # HTTP GET
data_terjemah = response_terjemah.json()     # konversi ke JSON
ayat_terjemah = (data_terjemah['data']['text'])

print (f"Ayat :")
print (ayat_arab)
print ("\nTerjemah :")
print (ayat_terjemah)
