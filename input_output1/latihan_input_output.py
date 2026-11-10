nama = input("Masukkan Nama : ")
nim = input("Masukkan Nim : ")
prodi = input("Masukkan Prodi : ")
status_input = int(input("Masukkan Status 1 (aktif) 0 (Non aktif): "))

status = bool(status_input)

print("// Data Mahasiswa //")
print("Nama :", nama)
print("NIM :", nim)
print("Prodi :", prodi)
print("Status :", status)