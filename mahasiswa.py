from sys import exit
import json


def dataMentah(mahasiswa: dict) -> dict:
    simpan = {}
    n = input("Masukan NIM : ")
    if n not in mahasiswa: 
        nama = input("Masukan Nama : ")
        asal = input("Masukan Asal : ")
        simpan["Nama"] = nama
        simpan["Asal"] = asal
        mahasiswa[n] = simpan
    return mahasiswa         

# json buat, baca, bahrui, hapus data
def buat_json(mahasiswa):
    data = json.dumps(mahasiswa, indent=4)
    with open("sample.json", "w") as f:
	    f.write(data)

def baca_json():
    with open('sample.json', 'r') as openfile:
	    data = json.load(openfile)
    return data

def update():
    pass

def hapus():
    pass


def main(mahasiswa: dict):
    while True:
        print("\n1. Buat")
        print("2. Tampil")
        print("3. Hapus")
        print("0. Keluar\n")
        p = int(input("Masukan Pilihan : "))
        if p == 1:
            dataMentah(mahasiswa)
            buat_json(mahasiswa)
        if p == 2:
            n = input("Masukan NIM : ")
            if n in mahasiswa:
                print(mahasiswa[n])
            else:
                print("Data tidak tersedia")
        if p == 3:
            print(mahasiswa)
            n = input("Masukan NIM : ")
            if n in mahasiswa:
                del mahasiswa[n]
                print("Data terhapus")
        if p == 0:
            break



if __name__=="__main__":
    mahasiswa = {} 
    main(mahasiswa)
    print(baca_json())
    exit()



















