from tkinter import*
import tkinter.messagebox
from AdminController import AdminController



class ViewUpdateUser:

    def __init__(self, root, username):
        self.root = root
        self.username=username
        self.root.Title="Update User"
        lebar=600
        tinggi=470
        setTengahX = (self.root.winfo_screenwidth()-lebar)//2
        setTengahY = (self.root.winfo_screenheight()-tinggi)//2
        self.root.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))
        self.Komponen()
        self.LihatUser()
        
    def LihatUser(self):
        admin=AdminController("admin")
        detail=admin.LihatUser(self.username)
        #self.entId.insert(END, detail['idbarang'])
        self.entNama.insert(END, detail['name'])
        self.entTelp.insert(END, detail['telp'])
        self.entAlamat.insert(END, detail['address'])
        self.entPosisi.insert(END, detail['position'])
        self.entEmail.insert(END, detail['email'])
        self.entRole.insert(END, detail['role'])
    
    def UpdateBarang(self):
        admin=AdminController("admin")
        admin.UpdateUser(self.username,self.entPass.get(), self.entNama.get(), self.entTelp.get(), self.entAlamat.get(), self.entPosisi.get(), self.entEmail.get(), self.entRole.get())
        
    
    def Komponen(self):
        Title=Label(self.root, bg="#666", text='Perbarui Data User', font=('arial',20, 'bold'))
        Title.pack(fill=X, side=TOP)

        MainFrame=Frame(self.root)
        MainFrame.pack(fill=X, side=TOP, pady=30)

        ButtonFrame=Frame(self.root)
        ButtonFrame.pack(fill=X, side=TOP)
    
        Label(MainFrame, text='Username', font=(25), width=25).grid(row=1, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=1, column=1, sticky=W,pady=5,padx=10)
        self.entUsername = Label(MainFrame, width=25, font=(25), text=str(self.username))
        self.entUsername.grid(row=1, column=2,sticky=W)

        Label(MainFrame, text='Password', font=(25), width=25).grid(row=2, column=0, sticky=W,padx=20)
        Label(MainFrame, text=':', font=(25)).grid(row=2, column=1, sticky=W,pady=5,padx=10)
        self.entPass = Entry(MainFrame, width=25, font=(25), text="*****")
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
        
        ButtonUpdate=Button(ButtonFrame, text='Perbarui', font=('arial',18,'bold'), padx=10, pady=10,command=self.UpdateBarang)
        ButtonUpdate.pack(side=TOP, pady=30)
    
def main(username):
    root=Tk()
    application=ViewUpdateUser(root, username)
    root.mainloop()

