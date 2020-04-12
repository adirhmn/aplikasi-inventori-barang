from tkinter import*
import tkinter.messagebox
from AdminController import AdminController



class ViewDetailUser:

    def __init__(self, root, username):
        self.root = root
        self.username=username
        self.root.Title="Detail User"
        lebar=600
        tinggi=400
        setTengahX = (self.root.winfo_screenwidth()-lebar)//2
        setTengahY = (self.root.winfo_screenheight()-tinggi)//2
        self.root.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))
        self.Komponen()

    
    
    def Komponen(self):
        admin=AdminController("admin")
        detail=admin.LihatUser(self.username)
        self.username=str(detail['username'])
        self.password=str(detail['password'])
        self.nama=str(detail['name'])
        self.telp=str(detail['telp'])
        self.alamat=str(detail['address'])
        self.posisi=str(detail['position'])
        self.email=str(detail['email'])
        self.role=str(detail['role'])

        Title=Label(self.root, bg="#666", text='Detail', font=('arial',20, 'bold'))
        Title.pack(fill=X, side=TOP)

        MainFrame=Frame(self.root)
        MainFrame.pack(fill=X, side=TOP, pady=30)

        ButtonFrame=Frame(self.root)
        ButtonFrame.pack(fill=X, side=TOP)
    
        Label(MainFrame, text='Username', font=(25), width=25).grid(row=1, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=1, column=1, sticky=W,pady=5,padx=10)
        self.entUsername = Label(MainFrame, width=25, font=(25), text=self.username)
        self.entUsername.grid(row=1, column=2,sticky=W)

        Label(MainFrame, text='Password', font=(25), width=25).grid(row=2, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=2, column=1, sticky=W,pady=5,padx=10)
        self.entPass = Label(MainFrame, width=25, font=(25), text=self.password)
        self.entPass.grid(row=2, column=2,sticky=W)

        Label(MainFrame, text='Nama', font=(25), width=25).grid(row=3, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=3, column=1, sticky=W,pady=5,padx=10)
        self.entNama = Label(MainFrame, width=25, font=(25), text=self.nama)
        self.entNama.grid(row=3, column=2,sticky=W)
        
        Label(MainFrame, text='Nomor Telepon', font=(25), width=25).grid(row=4, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=4, column=1, sticky=W,pady=5,padx=10)
        self.entTelp = Label(MainFrame, width=25, font=(25), text=self.telp)
        self.entTelp.grid(row=4, column=2,sticky=W)

        Label(MainFrame, text='Alamat', font=(25), width=25).grid(row=5, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=5, column=1, sticky=W,pady=5,padx=10)
        self.entAlamat = Label(MainFrame, width=25, font=(25), text=self.alamat)
        self.entAlamat.grid(row=5, column=2,sticky=W)

        Label(MainFrame, text='Posisi', font=(25), width=25).grid(row=6, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=6, column=1, sticky=W,pady=5,padx=10)
        self.entPosisi = Label(MainFrame, width=25, font=(25), text=self.posisi)
        self.entPosisi.grid(row=6, column=2,sticky=W)

        Label(MainFrame, text='Email', font=(25), width=25).grid(row=7, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=7, column=1, sticky=W,pady=5,padx=10)
        self.entEmail = Label(MainFrame, width=25, font=(25), text=self.email)
        self.entEmail.grid(row=7, column=2,sticky=W)

        Label(MainFrame, text='Login Sebagai', font=(25), width=25).grid(row=6, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=6, column=1, sticky=W,pady=5,padx=10)
        self.entRole = Label(MainFrame, width=25, font=(25), text=self.role)
        self.entRole.grid(row=6, column=2,sticky=W)
        

    
def main(username):
    root=Tk()
    application=ViewDetailUser(root,username)
    root.mainloop()

#main()