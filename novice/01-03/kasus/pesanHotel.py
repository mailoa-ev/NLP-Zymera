class Pesan:
    def __init__(self):
        print("Ini class Order")

    def setOrder(self, noPesan, tglPesan, checkIn, checkOut, bykTamu):
        Pesan.nomorPesanan = noPesan
        Pesan.tanggalPesan = tglPesan
        Pesan.tanggalMasuk = checkIn
        Pesan.tanggalKeluar = checkOut
        Pesan.jumlahTamu = bykTamu

    def getOrder(self):
        print("ID Pesanan Kamar       = ", Pesan.nomorPesanan)
        print("Tanggal Pesan       = ", Pesan.tanggalPesan)
        print("Tanggal Check In   = ", Pesan.tanggalMasuk)
        print("Tanggal Check Out  = ", Pesan.tanggalKeluar)
        print("Jumlah Tamu = ", Pesan.jumlahTamu)
