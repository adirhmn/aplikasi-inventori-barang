from tkinter import*
import tkinter.messagebox
from AdminController import AdminController



class ViewTambahUser:

    def __init__(self, root):
        self.root = root
        self.root.Title="Edit Data Barang"
        lebar=600
        tinggi=470
        setTengahX = (self.root.winfo_screenwidth()-lebar)//2
        setTengahY = (self.root.winfo_screenheight()-tinggi)//2
        self.root.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))
        self.Komponen()
        
    def TambahUser(self):
        user=AdminController("admin")
        user.TambahUser(self.entUsername.get(),self.entPass.get(), self.entNama.get(), self.entTelp.get(), self.entAlamat.get(), self.entPosisi.get(), self.entEmail.get(), self.entRole.get())
        self.entUsername.delete(0, END)
        self.entPass.delete(0, END)
        self.entNama.delete(0, END)
        self.entTelp.delete(0, END)
        self.entAlamat.delete(0, END)
        self.entPosisi.delete(0, END)
        self.entEmail.delete(0, END)
        self.entRole.delete(0, END)
    
    def Komponen(self):
        Title=Label(self.root, bg="#666", text='Tambah User', font=('arial',20, 'bold'))
        Title.pack(fill=X, side=TOP)

        MainFrame=Frame(self.root)
        MainFrame.pack(fill=X, side=TOP, pady=30)

        ButtonFrame=Frame(self.root)
        ButtonFrame.pack(fill=X, side=TOP)
    
        Label(MainFrame, text='Username', font=(25), width=25).grid(row=1, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=1, column=1, sticky=W,pady=5,padx=10)
        self.entUsername = Entry(MainFrame, width=25, font=(25))
        self.entUsername.grid(row=1, column=2,sticky=W)

        Label(MainFrame, text='Password', font=(25), width=25).grid(row=2, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=2, column=1, sticky=W,pady=5,padx=10)
        self.entPass = Entry(MainFrame, width=25, font=(25))
        self.entPass.grid(row=2, column=2,sticky=W)

        Label(MainFrame, text='Nama', font=(25), width=25).grid(row=3, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=3, column=1, sticky=W,pady=5,padx=10)
        self.entNama = Entry(MainFrame, width=25, font=(25))
        self.entNama.grid(row=3, column=2,sticky=W)
        
        Label(MainFrame, text='Nomor Telepon', font=(25), width=25).grid(row=4, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=4, column=1, sticky=W,pady=5,padx=10)
        self.entTelp = Entry(MainFrame, width=25, font=(25))
        self.entTelp.grid(row=4, column=2,sticky=W)

        Label(MainFrame, text='Alamat', font=(25), width=25).grid(row=5, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=5, column=1, sticky=W,pady=5,padx=10)
        self.entAlamat = Entry(MainFrame, width=25, font=(25))
        self.entAlamat.grid(row=5, column=2,sticky=W)

        Label(MainFrame, text='Posisi', font=(25), width=25).grid(row=6, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=6, column=1, sticky=W,pady=5,padx=10)
        self.entPosisi = Entry(MainFrame, width=25, font=(25))
        self.entPosisi.grid(row=6, column=2,sticky=W)

        Label(MainFrame, text='Email', font=(25), width=25).grid(row=7, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=7, column=1, sticky=W,pady=5,padx=10)
        self.entEmail = Entry(MainFrame, width=25, font=(25))
        self.entEmail.grid(row=7, column=2,sticky=W)

        Label(MainFrame, text='Login Sebagai', font=(25), width=25).grid(row=8, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=8, column=1, sticky=W,pady=5,padx=10)
        self.entRole = Entry(MainFrame, width=25, font=(25))
        self.entRole.grid(row=8, column=2,sticky=W)
        
        ButtonTambah=Button(ButtonFrame, text='Tambah', font=('arial',18,'bold'), padx=10, pady=10, command=self.TambahUser)
        ButtonTambah.pack(side=TOP, pady=30)
    
def main():
    root=Tk()
    application=ViewTambahUser(root)
    root.mainloop()

