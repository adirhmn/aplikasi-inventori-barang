from tkinter import*
import tkinter.messagebox

class HomeAdmin:

    def __init__(self, root):
        self.root = root
        lebar=1350
        tinggi=750
        setTengahX = (self.root.winfo_screenwidth()-lebar)//2
        setTengahY = (self.root.winfo_screenheight()-tinggi)//2
        self.root.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))
        self.root.title("Sistem Informasi Inventori Barang")
        self.root.attributes('-fullscreen', True)
        self.Frame()

    def Exit(self):
        Exit=tkinter.messagebox.askyesno("Sistem Inventori Barang", "Apakah Anda Yakin Akan Keluar?")
        if Exit>0:
            self.root.destroy()
            import ViewLogin
            ViewLogin.main()
            return

    def btnDataBarang(self):
        self.root.destroy()
        import ViewDataBarang
        ViewDataBarang.main()
    
    def btnDataLaporan(self):
        self.root.destroy()
        import ViewDataLaporan
        ViewDataLaporan.main()

    def btnDataUser(self):
        self.root.destroy()
        import ViewDataUser
        ViewDataUser.main()
    
    
        
    def Frame(self):
        #=======================================Frames==============================
        MainFrame=Frame(self.root, bg="lavender")
        MainFrame.pack(fill=X)

        TitFrame=Frame(MainFrame, bd=2, padx=8, pady=8, bg="lavender", relief=FLAT) 
        TitFrame.pack(fill=X, side=TOP)

        Title=Label(TitFrame, font=('verdana', 20, 'bold'), text="Sistem Informasi Inventori Barang", bg="lavender")
        Title.pack()

        ButtonFrame=Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost White", relief=FLAT)
        ButtonFrame.pack(fill=X, side=TOP, pady=10)

        FirstFrame=Frame(MainFrame, bd=1,width=1300, height=450, padx=20, pady=20, relief=RIDGE, bg="lavender") 
        FirstFrame.pack(side=BOTTOM)

        Intro=Label(FirstFrame, font=('verdana', 12, 'bold'), text="Halo Admin, \n selamat datang di Sistem Informasi Inventori Barang. Aplikasi ini dapat membantu mengakses informasi terkait \n barang yang berada di gudang, melakukan penambahan barang, dan melakukan pengurangan barang. \n saat ini anda login sebgaai Admin", 
                        bg="#FAFAD2" )
        Intro.pack(side=TOP, fill=Y, pady=100)

        #=======================================Button Widget==============================
        self.btnHome=Button(ButtonFrame, text="Beranda", font=('arial', 16, 'bold'), height=1, width=10, bd=4, relief=GROOVE, bg="#20B2AA")
        self.btnHome.grid(row=0, column=0)

        self.btnDataBarang=Button(ButtonFrame, text="Data Barang", font=('arial', 16, 'bold'), height=1, width=10, bd=4, relief=FLAT, bg="#20B2AA",command=self.btnDataBarang)
        self.btnDataBarang.grid(row=0, column=1)

        self.btnDataLaporan=Button(ButtonFrame, text="Data Laporan", font=('arial', 16, 'bold'), height=1, width=10, bd=4, relief=FLAT, bg="#20B2AA", command=self.btnDataLaporan)
        self.btnDataLaporan.grid(row=0, column=2)

        self.btnDataUser=Button(ButtonFrame, text="Data User", font=('arial', 16, 'bold'), height=1, width=10, bd=4, relief=FLAT, bg="#20B2AA", command=self.btnDataUser)
        self.btnDataUser.grid(row=0, column=3)

        self.btnKeluar=Button(TitFrame, text="Keluar", font=('arial', 16, 'bold'), height=1, width=10, bd=4, relief=FLAT, bg="#F08080", command=self.Exit)
        self.btnKeluar.pack(side=RIGHT)

def main():
    root=Tk()
    app=HomeAdmin(root)
    root.mainloop()

if __name__=='__main__':
    root=Tk()
    app=HomeAdmin(root)
    root.mainloop()

