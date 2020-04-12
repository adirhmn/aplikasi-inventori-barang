import tkinter as tk
from tkinter import *
from tkinter import ttk


class SplashScreen:
    def __init__(self, root):
        self.root = root
        self.aturWindow()
 
 
    def aturWindow(self):
        # ambil ukuran dari file image
        lebar = 300
        tinggi = 100
        
        setengahLebar = (self.root.winfo_screenwidth()-lebar)//2
        setengahTinggi = (self.root.winfo_screenheight()-tinggi)//2
 
        # atur posisi window di tengah-tengah layar
        self.root.geometry("%ix%i+%i+%i" %(lebar, tinggi,setengahLebar,setengahTinggi))
 
        # atur Image via Komponen Label
        Label(self.root,  text="Loading",bg="Ghost White",fg="black", font=("Helvetica", 20), width=9, height=2).pack(side=TOP,anchor=N,fill=X)
        s = ttk.Style()
        s.theme_use('alt')
        s.configure("red.Horizontal.TProgressbar", background='#444', foreground="white", relief=FLAT,bd=0,height=2)
        
        self.progress = ttk.Progressbar(self.root, style="red.Horizontal.TProgressbar",orient="horizontal",length=600, mode="determinate")
        self.progress.pack(side=TOP,anchor=N,padx=10)
        self.bytes = 0
        self.maxbytes = 0
        self.start()
        
    def start(self):
        self.progress["value"] = 0
        self.maxbytes = 50000
        self.progress["maximum"] = 50000
        self.read_bytes()
        if self.progress["value"] == 60000:
            self.root.destroy()
            import ViewLogin
            ViewLogin.main()
                
    def read_bytes(self):
        '''simulate reading 500 bytes; update progress bar'''
        #self.bytes += 40+self.bytes
        self.bytes += 1000
        self.progress["value"] = self.bytes
        self.progress.after(100, self.start)
        
        
if __name__=='__main__':
    root = Tk()
    root.configure(bg="GhostWhite")
    # menghilangkan judul dan batas frame Window
    root.overrideredirect(True)
    SplashScreen(root)
    root.mainloop()



