""""data pembelian barang"""
nama_barang=input("Masukkan nama barang: ")
jumlah_barang=int(input("Masukkan jumlah barang: "))
harga_barang=float(input("Masukkan harga barang: "))

pembelian={
    "nama": nama_barang,
    "jumlah": jumlah_barang,
    "harga": harga_barang
}
print("Nama barang yang dibeli:", pembelian["nama"])
print("Jumlah barang yang dibeli:", pembelian["jumlah"])
print("Harganya:", pembelian["harga"])

"""nama-nama hari"""
nama_hari=input("Masukkan nama-nama hari:").split()
print("Nama-nama hari", nama_hari)

"""nama dan keanggotaan"""
nama_anggota=input("Masukkan nama anggota:")
status=str(input("Apakah status keanggotaan aktif ? ya/tidak:"))

keanggotaan={
    "nama": nama_anggota,
    "status":status== "ya"
}
print("Nama Anggota:", keanggotaan["nama"])
print("Status:", keanggotaan["status"])
