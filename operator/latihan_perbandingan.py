"""Perbandingan"""
a= int(input("Masukkan nilai a: "))
b= int(input("Masukkan nilai b: "))


print(f"Apakah {a} sama dengan {b}? {a==b}")
print(f"Apakah {a} tidak sama dengan {b}? {a!=b}")
print(f"Apakah {a} lebih besar dari {b}? {a>b}")
print(f"Apakah {a} lebih kecil dari {b}? {a<b}")
print(f"Apakah {a} lebih besar atau sama dengan {b}? {a>=b}")
print(f"Apakah {a} lebih kecil atau sama dengan {b}? {a<=b}")

"""Latihan Perbandingan"""
harga=float(input("Masukkan harga barang yang mau dibeli: "))
saldo=float(input("Masukkan saldo yang kamu punya: "))

ya = saldo>=harga

print(f"Apakah saldo {saldo} cukup untuk membeli barang dengan harga {harga}? {ya}")
sisa_saldo=saldo-harga
print(f"Sisa saldo {sisa_saldo}")
    