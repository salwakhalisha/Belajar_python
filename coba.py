nama_anggota=input("Masukkan Nama Anggota:")
status=str(input("Apakah Status Keanggotaan Aktif? ya/tidak:"))

keanggotaan={
    "nama": nama_anggota,
    "status": status == "ya"
}

print("Nama Anggota", keanggotaan["nama"])
print("Status", keanggotaan["status"])