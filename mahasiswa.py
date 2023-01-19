from sys import exit
from crud_json import setDataJsonFile, getDataJsonFile
import json, pprint


def addNewData() -> dict:
    nama = input("Masukan Nama : ")
    asal = input("Masukan Asal : ")
    return {"Nama":nama, "Asal":asal}

def main(mahasiswa: dict):
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
            setDataJsonFile(mahasiswa, "db.json")
        if p == 2:
            pp.pprint(getDataJsonFile("db.json"))
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



















