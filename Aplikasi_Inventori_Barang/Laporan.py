from pymongo import MongoClient

class Laporan:
    def __init__(self, idlaporan=None):
        ip='127.0.0.1'
        port=27017
        client=MongoClient(ip, port)
        dbName=client["databasebarang"]
        self.colreports=dbName["laporan"]
        if idlaporan:
            self.idlaporan=idlaporan
    
    def addLaporan(self, idlaporan, tanggal, jenis_laporan, catatan):
        laporan_attr={"idlaporan": idlaporan, "tanggal": tanggal, "jenis_laporan": jenis_laporan, "catatan": catatan}
        return self.colreports.insert_one(laporan_attr)
    

    def getIdLaporan(self):
        return self.idlaporan
    
    def setIdLaporan(self, idlaporan):
        set_id={"$set" :{"idlaporan": idlaporan}}
        return self.colreports.update_one({"idlaporan": self.idlaporan}, set_id)
    
    def getTanggal(self):
        get_tanggal=self.colreports.find_one({"idlaporan":self.idlaporan})
        return get_tanggal['tanggal'] 
    
    def setTanggal(self, tanggal):
        set_tanggal={"$set": {"tanggal":tanggal}}
        return self.colreports.update_one({"idlaporan":self.idlaporan}, set_tanggal)
    
    def getJenis(self):
        get_jenis=self.colreports.find_one({"idlaporan":self.idlaporan})
        return get_jenis['jenis'] 
    
    def setJenis(self, jenis):
        set_jenis={"$set": {"jenis":jenis}}
        return self.colreports.update_one({"idlaporan":self.idlaporan}, set_jenis)
    
    def getCatatan(self):
        get_catatan=self.colreports.find_one({"idlaporan":self.idlaporan})
        return get_catatan['catatan'] 
    
    def setCatatan(self, catatan):
        set_catatan={"$set": {"catatan":catatan}}
        return self.colreports.update_one({"idlaporan":self.idlaporan}, set_catatan)
    
    def updateLaporan(self, tanggal, jenis, catatan):
        update_laporan={"$set": {"tanggal": tanggal, "jenis_laporan": jenis, "catatan": catatan}}
        return self.colreports.update_one({"idlaporan":self.idlaporan}, update_laporan)
    
    def deleteLaporan(self):
        del_laporan={"idlaporan": self.idlaporan}
        return self.colreports.delete_one(del_laporan)
    
    def getDataLaporan(self):
        return self.colreports.find_one({"idlaporan":self.idlaporan})
    
    def getAllLaporan(self):
        reports=self.colreports.find()
        list_laporan=[]
        for report in reports:
            list_laporan.append(report)
        return list_laporan


