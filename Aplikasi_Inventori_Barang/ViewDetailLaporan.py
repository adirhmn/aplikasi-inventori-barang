from tkinter import*
import tkinter.messagebox
from AdminController import AdminController



class ViewDetailLaporan:

    def __init__(self, root, idlaporan):
        self.root = root
        self.idlaporan=idlaporan
        self.root.Title="Detail Laporan"
        lebar=600
        tinggi=400
        setTengahX = (self.root.winfo_screenwidth()-lebar)//2
        setTengahY = (self.root.winfo_screenheight()-tinggi)//2
        self.root.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))
        self.Komponen()

    
    def Komponen(self):
        admin=AdminController("admin")
        detail=admin.LihatLaporan(self.idlaporan)
        self.idlaporan=str(detail['idlaporan'])
        self.tanggal=str(detail['tanggal'])
        self.jenis=str(detail['jenis_laporan'])
        self.catatan=str(detail['catatan'])

        Title=Label(self.root, bg="#666", text='Detail', font=('arial',20, 'bold'))
        Title.pack(fill=X, side=TOP)

        MainFrame=Frame(self.root)
        MainFrame.pack(fill=X, side=TOP, pady=30)

        ButtonFrame=Frame(self.root)
        ButtonFrame.pack(fill=X, side=TOP)
    
        Label(MainFrame, text='ID Laporan', font=(25), width=25).grid(row=1, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=1, column=1, sticky=W,pady=5,padx=10)
        self.entIdLap = Label(MainFrame, width=25, font=(25), text=self.idlaporan)
        self.entIdLap.grid(row=1, column=2,sticky=W)

        Label(MainFrame, text='Tanggal', font=(25), width=25).grid(row=2, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=2, column=1, sticky=W,pady=5,padx=10)
        self.entTanggal = Label(MainFrame, width=25, font=(25), text=self.tanggal)
        self.entTanggal.grid(row=2, column=2,sticky=W)

        Label(MainFrame, text='Jenis Laporan', font=(25), width=25).grid(row=3, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=3, column=1, sticky=W,pady=5,padx=10)
        self.entJenis = Label(MainFrame, width=25, font=(25), text=self.jenis)
        self.entJenis.grid(row=3, column=2,sticky=W)
        
        Label(MainFrame, text='Catatan', font=(25), width=25).grid(row=4, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=4, column=1, sticky=W,pady=5,padx=10)
        self.entCatatan = Label(MainFrame, width=25, font=(25), text=self.catatan)
        self.entCatatan.grid(row=4, column=2,sticky=W)        

    
def main(username):
    root=Tk()
    application=ViewDetailLaporan(root,username)
    root.mainloop()

#main()