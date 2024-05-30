import os
os.system("cls")

print(f"|Tugas Akhir Makul Algoritma dan Pemrograman|")
print("Nama\t: M. Falih Daffa S")
print("NIM\t: 22.230.0136")
print("Kelas\t: 1P51\n")
list_nama = []
list_tanggal = []
list_harga = []
list_jumlah = []
gudang = None
x = 0

class Kelolagudang :
    def __init__(self, nama, tanggal, harga, jumlah):
        self.nama = nama
        list_nama.append(self.nama)
        self.tanggal = tanggal
        list_tanggal.append(self.tanggal)
        self.harga = harga
        list_harga.append(self.harga)
        self.jumlah = jumlah
        list_jumlah.append(self.jumlah)
    def tampildata (self):
        n = 0
        for i in range(x):
            n += 1
            print(f"{'-'*15}Data Barang {n}{'-'*15}")
            print(f"Nama barang\t\t :",list_nama[i])
            print("Tanggal barang masuk\t :",list_tanggal[i])
            print("Jumlah barang\t\t :",list_jumlah[i])
            print("Harga barang\t\t : Rp",list_harga[i])
    def cekBarang (self):
        print(f"{'-'*15}Data Barang {n+1}{'-'*15}")
        print("Nama barang\t\t :",list_nama[n])
        print("Tanggal barang masuk\t :",list_tanggal[n])
        print("Jumlah barang\t\t :",list_jumlah[n])
        print("Harga barang\t\t :Rp",list_harga[n])
    def updateBarang(self):
        gudang.cekBarang()
        print("[1] Tambah Jumlah Barang")
        print("[2] Kurangi Jumlah Barang")
        update = int(input("Masukkan pilihan anda : "))
        if update == 1:
            list_jumlah[n] += int(input("Tambahkan jumlah barang : "))
            print("\n*Barang sudah diupdate*")
            gudang.cekBarang()
        elif update == 2:
            list_jumlah[n] -= int(input("Kurangi jumlah barang : "))
            print("\n*Barang sudah diupdate*\n")
            gudang.cekBarang()
        else:
            print("Pilihan tidak tersedia")
while True :
    print(f"{'-'*15}Menu Gudang{'-'*15}")
    print("Silahkan pilih opsi")
    print("[1] Tambah barang")
    print("[2] Cek barang")
    print("[3] Update Ketersediaan barang")
    print("[4] Tampilkan semua data barang")
    print("[x] Keluar")
    opsi = input("Pilih opsi : ")
    print('-'*41)

    if opsi == 'x':
        print(f"\n{'='*17}Bye Bye{'='*17}\n")
        break

    elif opsi == '1':
        ulang = True
        while True:
            print(f"\n{'='*15}Tambah Barang{'='*15}\n")
            nama = input('Masukkan nama barang : ')
            tanggal = input("Masukkan tanggal barang masuk(ddmmyy) : ")
            jumlah = int(input("Masukkan jumlah barang : "))
            harga = int(input("Masukkan Harga : "))
            gudang = Kelolagudang(nama,tanggal,harga,jumlah)
            x += 1
            ulang = input('Input lagi ? (y/t) : ')
            if ulang == 't':
                print(f"{'='*43}\n")
                input("Tekan [Enter] untuk kembali ke menu")
                print("")
                break
            else:
                ulang == True

    elif opsi == '2':
        print(f"\n{'='*15}Cek Barang{'='*15}\n")
        cek_nama = input("Masukkan nama barang yang ingin dicek : ")
        if cek_nama in list_nama:
            print('\nBarang tersedia')
            n = list_nama.index(cek_nama)
            gudang.cekBarang()
        else:
            print("\nBarang tidak ditemukan")
        input("\nTekan [Enter] untuk kembali ke menu")
        print("")
        
    elif opsi == '3':
        print(f"\n{'='*15}Cek Barang{'='*15}\n")
        cek_nama = input("Masukkan nama barang yang ingin diupdate : ")
        if cek_nama in list_nama:
            print('\nBarang tersedia\n')
            print("Kode barang = ",list_nama.index(cek_nama))
            n = list_nama.index(cek_nama)
            gudang.updateBarang()
        else:
            print("Barang tidak ditemukan")
        input("\nTekan [Enter] untuk kembali ke menu")
        print("")

    elif opsi == '4':
        print(f"\n{'='*15}Daftar Barang{'='*15}\n")
        if gudang == None:
            print("Data barang kosong\nAnda belum menambahkan data barang\n")
        else:
            gudang.tampildata()
        print(f"{'='*43}\n")
        input("Tekan [Enter] untuk kembali ke menu")
        print("")
    else:
        print("Pilihan tidak tersedia")
