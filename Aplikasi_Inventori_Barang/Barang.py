from pymongo import MongoClient

class Barang:
    def __init__(self, idbarang=None):
        ip='127.0.0.1'
        port=27017
        client=MongoClient(ip, port)
        dbName=client["databasebarang"]
        self.colproducts=dbName["barang"]
        if idbarang:
            self.idbarang=idbarang
    
    def addData(self, idbarang, nama, jenis, stok, satuan, harga):
        product_attr={"idbarang": idbarang, "nama_barang": nama, "jenis_barang": jenis, "stok_barang": stok, "satuan":satuan, "harga": harga}
        return self.colproducts.insert_one(product_attr)
    
    def getIdBarang(self):
        return self.idbarang
    
    def setIdBarang(self, idbarang):
        set_id={"$set": {"idbarang":idbarang}}
        return self.colproducts.update_one({"idbarang":self.idbarang}, set_id)
    
    def getNama(self):
        get_nama=self.colproducts.find_one({"idbarang":self.idbarang})
        return get_nama['nama_barang'] 
    
    def setNama(self, nama_barang):
        set_nama={"$set": {"nama_barang":nama_barang}}
        return self.colproducts.update_one({"idbarang":self.idbarang}, set_nama)
    
    def getJenis(self):
        get_jenis=self.colproducts.find_one({"idbarang":self.idbarang})
        return get_jenis['jenis_barang'] 
    
    def setJenis(self, jenis_barang):
        set_jenis={"$set": {"jenis_barang":jenis_barang}}
        return self.colproducts.update_one({"idbarang":self.idbarang}, set_jenis)
    
    def getStok(self):
        get_stok=self.colproducts.find_one({"idbarang":self.idbarang})
        return get_stok['stok_barang'] 
    
    def setStok(self, stok):
        set_stok={"$set": {"stok_barang":stok}}
        return self.colproducts.update_one({"idbarang":self.idbarang}, set_stok)
    
    def getSatuan(self):
        get_satuan=self.colproducts.find_one({"idbarang":self.idbarang})
        return get_satuan['satuan'] 
    
    def setSatuan(self, satuan):
        set_satuan={"$set": {"satuan":satuan}}
        return self.colproducts.update_one({"idbarang":self.idbarang}, set_satuan)
    
    def getHarga(self):
        get_harga=self.colproducts.find_one({"idbarang":self.idbarang})
        return get_harga['harga'] 
    
    def setHarga(self, harga):
        set_harga={"$set": {"harga":harga}}
        return self.colproducts.update_one({"idbarang":self.idbarang}, set_harga)
    
    def updateBarang(self, nama, jenis, stok, satuan, harga):
        update_barang={"$set": {"nama_barang": nama, "jenis_barang": jenis, "stok_barang": stok, "satuan":satuan, "harga": harga}}
        return self.colproducts.update_one({"idbarang":self.idbarang}, update_barang)
    
    def deleteBarang(self):
        del_barang={"idbarang": self.idbarang}
        return self.colproducts.delete_one(del_barang)
    
    def getDataBarang(self):
        return self.colproducts.find_one({"idbarang":self.idbarang})
    
    def getAllBarang(self):
        barangs=self.colproducts.find()
        list_barang=[]
        for barang in barangs:
            list_barang.append(barang)
        return list_barang
    



