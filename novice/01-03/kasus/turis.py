# class ini digunakan untuk mengimplementasikan
# CRC card ke source code python
class Turis:
    def __init__(self, nomorKTP, nama, email, nomorHP):
        self.noKTP = nomorKTP
        self.name = nama
        self.surel = email
        self.noHP = nomorHP

    def displayTuris(self):
        print(input("Nomor KTP : ", self.noKTP))
        print(input("Name : ", self.name))
        print(input("Email : ", self.surel))
        print(input("Nomor Telepon : ", self.noHP))
