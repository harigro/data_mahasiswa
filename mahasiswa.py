import json
import pprint
from sys import exit
from tinydb import TinyDB, where


def addNewData() -> dict:
    nama = input("Masukan Nama : ")
    asal = input("Masukan Asal : ")
    return {"Nama":nama, "Asal":asal}

def main(mahasiswa: dict):
    data = None
    db = TinyDB("database/mahasiswa.json")
    pp = pprint.PrettyPrinter(indent=4, sort_dicts=False)
    while True:
        print("\n1. Buat")
        print("2. Tampil")
        print("3. Hapus")
        print("0. Keluar\n")
        p = int(input("Masukan Pilihan : "))
        if p == 1:
            n = input("Masukan NIM : ")
            if n not in mahasiswa:
                umum = addNewData()
                mahasiswa[n] = umum
            else:
                print("Data tersedia")
            db.insert(mahasiswa)
        if p == 2:
            pp.pprint(db.all())
        if p == 3:
            pp.pprint(getDataJsonFile("db.json"))
            n = input("Masukan NIM : ")
            if n in mahasiswa:
                del mahasiswa[n]
                setDataJsonFile(mahasiswa, "db.json")
                print("Data terhapus")
            else:
                print("Data tidak tersedia")
        if p == 0:
            exit()



if __name__=="__main__":
    mahasiswa = {} 
    main(mahasiswa)

