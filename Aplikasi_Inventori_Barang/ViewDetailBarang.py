from tkinter import*
import tkinter.messagebox
from AdminController import AdminController



class ViewDetailBarang:

    def __init__(self, root, idbarang):
        self.root = root
        self.idbarang=idbarang
        self.root.Title="Detail Barang"
        lebar=600
        tinggi=400
        setTengahX = (self.root.winfo_screenwidth()-lebar)//2
        setTengahY = (self.root.winfo_screenheight()-tinggi)//2
        self.root.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))
        self.Komponen()

    
    
    def Komponen(self):
        admin=AdminController("admin")
        detail=admin.LihatBarang(self.idbarang)
        self.id=str(detail['idbarang'])
        self.nama=str(detail['nama_barang'])
        self.jenis=str(detail['jenis_barang'])
        self.stok=str(detail['stok_barang'])
        self.satuan=str(detail['satuan'])
        self.harga=str(detail['harga'])

        Title=Label(self.root, bg="#666", text='Detail', font=('arial',20, 'bold'))
        Title.pack(fill=X, side=TOP)

        MainFrame=Frame(self.root)
        MainFrame.pack(fill=X, side=TOP, pady=30)

        ButtonFrame=Frame(self.root)
        ButtonFrame.pack(fill=X, side=TOP)
    
        Label(MainFrame, text='ID Barang', font=(25), width=25).grid(row=1, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=1, column=1, sticky=W,pady=5,padx=10)
        self.entId = Label(MainFrame, width=25, font=(25), text=self.id)
        self.entId.grid(row=1, column=2,sticky=W)

        Label(MainFrame, text='Nama Barang', font=(25), width=25).grid(row=2, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=2, column=1, sticky=W,pady=5,padx=10)
        self.entNama = Label(MainFrame, width=25, font=(25), text=self.nama)
        self.entNama.grid(row=2, column=2,sticky=W)

        Label(MainFrame, text='Jenis Barang', font=(25), width=25).grid(row=3, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=3, column=1, sticky=W,pady=5,padx=10)
        self.entJenis = Label(MainFrame, width=25, font=(25), text=self.jenis)
        self.entJenis.grid(row=3, column=2,sticky=W)
        
        Label(MainFrame, text='Stok Barang', font=(25), width=25).grid(row=4, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=4, column=1, sticky=W,pady=5,padx=10)
        self.entStok = Label(MainFrame, width=25, font=(25), text=self.stok)
        self.entStok.grid(row=4, column=2,sticky=W)

        Label(MainFrame, text='Satuan', font=(25), width=25).grid(row=5, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=5, column=1, sticky=W,pady=5,padx=10)
        self.entSatuan = Label(MainFrame, width=25, font=(25), text=self.satuan)
        self.entSatuan.grid(row=5, column=2,sticky=W)

        Label(MainFrame, text='Harga Per Satuan', font=(25), width=25).grid(row=6, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=6, column=1, sticky=W,pady=5,padx=10)
        self.entHarga = Label(MainFrame, width=25, font=(25), text=self.harga)
        self.entHarga.grid(row=6, column=2,sticky=W)
        
        #ButtonTambah=Button(ButtonFrame, text='Tambah', font=('arial',18,'bold'), padx=10, pady=10)
        #ButtonTambah.pack(side=TOP, pady=30)
    
def main(id_barang):
    root=Tk()
    application=ViewDetailBarang(root,id_barang)
    root.mainloop()

#main()