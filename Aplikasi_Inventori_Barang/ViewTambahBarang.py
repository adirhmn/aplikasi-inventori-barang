from tkinter import*
import tkinter.messagebox
from AdminController import AdminController



class ViewTambahBarang:

    def __init__(self, root):
        self.root = root
        self.root.Title="Edit Data Barang"
        lebar=600
        tinggi=400
        setTengahX = (self.root.winfo_screenwidth()-lebar)//2
        setTengahY = (self.root.winfo_screenheight()-tinggi)//2
        self.root.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))
        self.Komponen()
        
    def TambahBarang(self):
        admin=AdminController("admin")
        admin.TambahBarang(self.entId.get(), self.entNama.get(), self.entJenis.get(), self.entStok.get(), self.entSatuan.get(), self.entHarga.get())
        self.entId.delete(0, END)
        self.entNama.delete(0, END)
        self.entJenis.delete(0, END)
        self.entStok.delete(0, END)
        self.entSatuan.delete(0, END)
        self.entHarga.delete(0, END)
    
    def Komponen(self):
        Title=Label(self.root, bg="#666", text='Edit Data Barang', font=('arial',20, 'bold'))
        Title.pack(fill=X, side=TOP)

        MainFrame=Frame(self.root)
        MainFrame.pack(fill=X, side=TOP, pady=30)

        ButtonFrame=Frame(self.root)
        ButtonFrame.pack(fill=X, side=TOP)
    
        Label(MainFrame, text='ID Barang', font=(25), width=25).grid(row=1, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=1, column=1, sticky=W,pady=5,padx=10)
        self.entId = Entry(MainFrame, width=25, font=(25))
        self.entId.grid(row=1, column=2,sticky=W)

        Label(MainFrame, text='Nama Barang', font=(25), width=25).grid(row=2, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=2, column=1, sticky=W,pady=5,padx=10)
        self.entNama = Entry(MainFrame, width=25, font=(25))
        self.entNama.grid(row=2, column=2,sticky=W)

        Label(MainFrame, text='Jenis Barang', font=(25), width=25).grid(row=3, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=3, column=1, sticky=W,pady=5,padx=10)
        self.entJenis = Entry(MainFrame, width=25, font=(25))
        self.entJenis.grid(row=3, column=2,sticky=W)
        
        Label(MainFrame, text='Stok Barang', font=(25), width=25).grid(row=4, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=4, column=1, sticky=W,pady=5,padx=10)
        self.entStok = Entry(MainFrame, width=25, font=(25))
        self.entStok.grid(row=4, column=2,sticky=W)

        Label(MainFrame, text='Satuan', font=(25), width=25).grid(row=5, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=5, column=1, sticky=W,pady=5,padx=10)
        self.entSatuan = Entry(MainFrame, width=25, font=(25))
        self.entSatuan.grid(row=5, column=2,sticky=W)

        Label(MainFrame, text='Harga Per Satuan', font=(25), width=25).grid(row=6, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=6, column=1, sticky=W,pady=5,padx=10)
        self.entHarga = Entry(MainFrame, width=25, font=(25))
        self.entHarga.grid(row=6, column=2,sticky=W)
        
        ButtonTambah=Button(ButtonFrame, text='Tambah', font=('arial',18,'bold'), padx=10, pady=10, command=self.TambahBarang)
        ButtonTambah.pack(side=TOP, pady=30)
    
def main():
    root=Tk()
    application=ViewTambahBarang(root)
    root.mainloop()

