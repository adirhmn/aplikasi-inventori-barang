from tkinter import*
import tkinter.messagebox
#import stdDatabase
from AdminController import AdminController

class ViewDataBarang:

    def __init__(self, root):
        self.root = root
        lebar=1350
        tinggi=750
        setTengahX = (self.root.winfo_screenwidth()-lebar)//2
        setTengahY = (self.root.winfo_screenheight()-tinggi)//2
        self.root.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))
        self.admin=AdminController("admin")
        self.root.attributes('-fullscreen', True)
        self.Frame()
    
    def Exit(self):
        Exit=tkinter.messagebox.askyesno("Sistem Inventori Barang", "Apakah Anda Yakin Akan Keluar?")
        if Exit>0:
            self.root.destroy()
            import ViewLogin
            ViewLogin.main()
            return
    
    def btnBeranda(self):
        self.root.destroy()
        import HomeAdmin
        HomeAdmin.main()
    
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

        MenuFrame=Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost White", relief=FLAT)
        MenuFrame.pack(fill=X, side=TOP, pady=10)

        DataFrame=LabelFrame(MainFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE, font=('arial', 20, 'bold'), text="Daftar Barang")
        DataFrame.pack(side=TOP)

        DataFrameLeft=Frame(DataFrame, height=20)
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight=Frame(DataFrame)
        DataFrameRight.pack(side=RIGHT,padx=200)

        ButtonFrame=Frame(MainFrame, bg='#666')
        ButtonFrame.pack(side=TOP)


        #=======================================ListBoc and ScrollBar Entry Widget==============================
        scrollbar=Scrollbar(DataFrameLeft)
        scrollbar.grid(row=0, column=1, sticky='ns')

        def LihatBarang():
            global br
            searchBrg=daftarbarang.curselection()[0]
            br=daftarbarang.get(searchBrg)
            id=br[0]
            import ViewDetailBarang
            ViewDetailBarang.main(id)

        def TambahBarang():
            import ViewTambahBarang
            ViewTambahBarang.main()
        
        def UpdateBarang():
            global br
            searchBrg=daftarbarang.curselection()[0]
            br=daftarbarang.get(searchBrg)
            id=br[0]
            import ViewUpdateBarang
            ViewUpdateBarang.main(id)

        def HapusBarang():
            global br
            searchBrg=daftarbarang.curselection()[0]
            br=daftarbarang.get(searchBrg)
            id=br[0]
            Hapus=tkinter.messagebox.askyesno("Hapus Barang", "Apakah Anda Yakin Akan Menghapus Item Ini?")
            if Hapus>0:
                self.admin.HapusBarang(id)
                ShowBarang()
                return
        
        def ShowBarang():
            barangs=self.admin.LihatSemuaBarang()
            daftarbarang.delete(0,END)
            for barang in barangs:
                daftarbarang.insert(END, (barang['idbarang'], barang['nama_barang']), str(""))

        daftarbarang=Listbox(DataFrameLeft, width=40, height=16, font=('arial', 22, 'bold'), yscrollcommand=scrollbar.set)
        daftarbarang.bind('<<ListboxSelect>>', LihatBarang)
        barangs=self.admin.LihatSemuaBarang()
        daftarbarang.delete(0,END)
        #daftarbarang.
        for barang in barangs:
            daftarbarang.insert(END, (barang['idbarang'], barang['nama_barang']), str(""))
        daftarbarang.grid(row=0, column=0, padx=8)
        scrollbar.config(command=daftarbarang.yview) 
 
        
        #=======================================Button Widget==============================
        self.btnHome=Button(MenuFrame, text="Beranda", font=('arial', 16, 'bold'), height=1, width=10, bd=4, relief=FLAT, bg="#20B2AA", command=self.btnBeranda)
        self.btnHome.grid(row=0, column=0)

        self.btnDataBarang=Button(MenuFrame, text="Data Barang", font=('arial', 16, 'bold'), height=1, width=10, bd=4, relief=GROOVE, bg="#20B2AA")
        self.btnDataBarang.grid(row=0, column=1)

        self.btnDataLaporan=Button(MenuFrame, text="Data Laporan", font=('arial', 16, 'bold'), height=1, width=10, bd=4, relief=FLAT, bg="#20B2AA", command=self.btnDataLaporan)
        self.btnDataLaporan.grid(row=0, column=2)

        self.btnDataUser=Button(MenuFrame, text="Data User", font=('arial', 16, 'bold'), height=1, width=10, bd=4, relief=FLAT, bg="#20B2AA", command=self.btnDataUser)
        self.btnDataUser.grid(row=0, column=3)

        self.btnKeluar=Button(TitFrame, text="Keluar", font=('arial', 16, 'bold'), height=1, width=10, bd=4, relief=FLAT, bg="#F08080", command=self.Exit)
        self.btnKeluar.pack(side=RIGHT)

        
        #======================================Button Aksi====================================

        self.btnRefreshData=Button(DataFrameRight, text="Refresh", font=('arial', 16, 'bold'),bg='Ghost White', height=1, width=10, bd=4, relief=FLAT, command=ShowBarang)
        self.btnRefreshData.pack(side=TOP, pady=10)
        
        self.btnDetailData=Button(DataFrameRight, text="Detail", font=('arial', 16, 'bold'),bg='Ghost White', height=1, width=10, bd=4, relief=FLAT, command=LihatBarang)
        self.btnDetailData.pack(side=TOP, pady=10)

        self.btnTambahData=Button(DataFrameRight, text="Tambah", font=('arial', 16, 'bold'),bg='Ghost White',  height=1, width=10, bd=4, relief=FLAT, command=TambahBarang)
        self.btnTambahData.pack(side=TOP, pady=10)

        self.btnPerbaruiData=Button(DataFrameRight, text="Perbarui", font=('arial', 16, 'bold'),bg='Ghost White', height=1, width=10, bd=4, relief=FLAT, command=UpdateBarang)
        self.btnPerbaruiData.pack(side=TOP, pady=10)

        self.btnHapusData=Button(DataFrameRight, text="Hapus", font=('arial', 16, 'bold'),bg='Ghost White', height=1, width=10, bd=4, relief=FLAT, command=HapusBarang)
        self.btnHapusData.pack(side=TOP, pady=10)

def main():
    root=Tk()
    application=ViewDataBarang(root)
    root.mainloop()




