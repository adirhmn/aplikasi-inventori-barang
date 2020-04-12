from tkinter import*
import tkinter.messagebox
from AdminController import AdminController



class ViewTambahLaporan:

    def __init__(self, root):
        self.root = root
        self.root.Title="Edit Laporan"
        lebar=600
        tinggi=400
        setTengahX = (self.root.winfo_screenwidth()-lebar)//2
        setTengahY = (self.root.winfo_screenheight()-tinggi)//2
        self.root.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))
        self.Komponen()
        
    def TambahUser(self):
        user=AdminController("admin")
        user.TambahLaporan(self.entIdLap.get(),self.entTgl.get(), self.entJenis.get(), self.entCatatan.get())
        self.entIdLap.delete(0, END)
        self.entTgl.delete(0, END)
        self.entJenis.delete(0, END)
        self.entCatatan.delete(0, END)
    
    def Komponen(self):
        Title=Label(self.root, bg="#666", text='Tambah Laporan', font=('arial',20, 'bold'))
        Title.pack(fill=X, side=TOP)

        MainFrame=Frame(self.root)
        MainFrame.pack(fill=X, side=TOP, pady=30)

        ButtonFrame=Frame(self.root)
        ButtonFrame.pack(fill=X, side=TOP)
    
        Label(MainFrame, text='ID Laporan', font=(25), width=25).grid(row=1, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=1, column=1, sticky=W,pady=5,padx=10)
        self.entIdLap = Entry(MainFrame, width=25, font=(25))
        self.entIdLap.grid(row=1, column=2,sticky=W)

        Label(MainFrame, text='Tanggal (dd/mm/yyyy)', font=(25), width=25).grid(row=2, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=2, column=1, sticky=W,pady=5,padx=10)
        self.entTgl = Entry(MainFrame, width=25, font=(25))
        self.entTgl.grid(row=2, column=2,sticky=W)

        Label(MainFrame, text='Jenis Laporan', font=(25), width=25).grid(row=3, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=3, column=1, sticky=W,pady=5,padx=10)
        self.entJenis = Entry(MainFrame, width=25, font=(25))
        self.entJenis.grid(row=3, column=2,sticky=W)
        
        Label(MainFrame, text='Catatan', font=(25), width=25).grid(row=4, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=4, column=1, sticky=W,pady=5,padx=10)
        self.entCatatan = Entry(MainFrame, width=25, font=(25))
        self.entCatatan.grid(row=4, column=2,sticky=W)
        
        ButtonTambah=Button(ButtonFrame, text='Tambah', font=('arial',18,'bold'), padx=10, pady=10, command=self.TambahUser)
        ButtonTambah.pack(side=TOP, pady=30)
    
def main():
    root=Tk()
    application=ViewTambahLaporan(root)
    root.mainloop()

