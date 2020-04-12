from User import User
from Barang import Barang
from Laporan import Laporan

class AdminController:
    def __init__(self, username):
        self.user=User(username)
        self.barang=Barang()
        self.laporan=Laporan()
    
    def TambahBarang(self, id_barang, nama_barang, jenis_barang, stok_barang, satuan_barang, harga_barang):
        return self.barang.addData(id_barang, nama_barang, jenis_barang, stok_barang, satuan_barang, harga_barang)
    
    def UpdateBarang(self,idbarang, nama_barang, jenis_barang, stok_barang, satuan_barang, harga_barang):
        barang=Barang(idbarang)
        return barang.updateBarang(nama_barang, jenis_barang, stok_barang, satuan_barang, harga_barang)
    
    def HapusBarang(self, idbarang):
        barang=Barang(idbarang)
        return barang.deleteBarang()
    
    def LihatSemuaBarang(self):
        return self.barang.getAllBarang()
    
    def LihatBarang(self, idbarang):
        barang=Barang(idbarang)
        return barang.getDataBarang()
    
    def TambahLaporan(self, idlaporan, tanggal, jenis_laporan, catatan):
        return self.laporan.addLaporan(idlaporan, tanggal, jenis_laporan, catatan)
    
    def UpdateLaporan(self,idlaporan, tanggal, jenis, catatan):
        laporan=Laporan(idlaporan)
        return laporan.updateLaporan(tanggal, jenis, catatan)
    
    def HapusLaporan(self, idlaporan):
        laporan=Laporan(idlaporan)
        return laporan.deleteLaporan()
    
    def LihatSemuaLaporan(self):
        return self.laporan.getAllLaporan()
    
    def LihatLaporan(self, idlaporan):
        laporan=Laporan(idlaporan)
        return laporan.getDataLaporan()






