from tkinter import*
from LoginController import LoginController
from PIL import ImageTk, Image
import os

class Login:

    def __init__(self, root):
        self.root = root
        lebar=700
        tinggi=470
        setTengahX = (self.root.winfo_screenwidth()-lebar)//2
        setTengahY = (self.root.winfo_screenheight()-tinggi)//2
        self.root.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))
        self.root.title("Sistem Informasi Inventori Barang")
        self.root.overrideredirect(1)
        self.Frame()
    
    def Exit(self):
        self.root.destroy()
    
    def CekLogin(self):
        cek=LoginController()
        role=cek.Login(self.entUsername.get(), self.entPassword.get())
        if role=="admin":
            self.root.destroy()
            import HomeAdmin
            HomeAdmin.main()
        elif role=="staff":
            self.root.destroy()
            import HomeStaff
            HomeStaff.main()
        else:
            self.root.destroy()
            import HomeGuest
            HomeGuest.main()
    
    def Guest(self):
        self.root.destroy()
        import HomeGuest
        HomeGuest.main()
    
    def Frame(self):
        TopFrame=Frame(self.root)
        TopFrame.pack(side=TOP, fill=X)
        ButtonExit=Button(TopFrame, text='X', font=('arial', 18, 'bold'),relief=FLAT,bg='red',fg='black', command=self.Exit)
        ButtonExit.pack(side=RIGHT)

        Title=Label(self.root, text="SELAMAT DATANG DI APLIKASI INVENTORI BARANG", font=(30))
        Title.pack(side=TOP, ipadx=20, ipady=50)

        FrameLogin=Frame(self.root, bg='#666')
        FrameLogin.pack(side=TOP, ipady=100, ipadx=100)

        TextUsername=Label(FrameLogin, bg='#666', text="Username", font=('arial',16, 'bold'))
        TextUsername.pack_configure(side=TOP, pady=10)
        self.entUsername=Entry(FrameLogin, width=20, font=(40))
        self.entUsername.pack(side=TOP, pady=5)

        TextUsername=Label(FrameLogin, bg='#666', text="Password", font=('arial',16, 'bold'))
        TextUsername.pack(side=TOP, pady=10)
        self.entPassword=Entry(FrameLogin,show='*', width=20, font=(40))
        self.entPassword.pack(side=TOP, pady=5)

        ButtonLogin=Button(FrameLogin, bg='Ghost White', text="Login", font=('arial',10, 'bold'), relief=FLAT, command=self.CekLogin)
        ButtonLogin.pack(side=TOP, pady=20, ipadx=20)

        ButtonTamu=Button(FrameLogin, bg='Ghost White', text="Saya adalah tamu", font=(20), relief=FLAT, command=self.Guest)
        ButtonTamu.pack(side=TOP, pady=20, ipadx=20)


def main():
    root=Tk()
    application=Login(root)
    root.mainloop()

