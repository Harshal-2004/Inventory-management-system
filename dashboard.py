from tkinter import *
from PIL import ImageTk
import PIL.Image
from tkinter.tix import *
import os
import webbrowser
from sale import saleClass 
from sold import soldClass
from stock import stockClass
from product import productClass
from tkinter import messagebox

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("IMS")
        self.root.config(bg="white")
        photo = PhotoImage(file = "images\i1.png")
        self.root.iconphoto(False, photo)


        #------Title-------
        self.icon_title = PhotoImage(file="images\icon1.png")
        title = Label(self.root, text="Inventory Management System", image=self.icon_title, compound=LEFT, font = ("times new roman", 37, "bold"), bg="midnight blue", fg="azure", anchor="w", padx=30).place(x=0, y=0, width=1350, height=90)

#---Clock---
		#self.lbl_clock = Label(self.root, text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font = ("times new roman", 15), bg="#4d636d", fg="white")
		#self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        #=========Left Menu==========
        self.MenuLogo = PIL.Image.open("images/l1.png")
        self.MenuLogo=self.MenuLogo.resize((200,200))
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root, bd=2, relief=RIDGE, bg="azure")
        LeftMenu.place(x=0,y=102, width=350, height=490)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20), bg="#009688").pack(side=TOP,fill=X)

        self.icon_side = PhotoImage(file="images\side1.png")

        btn_product = Button(LeftMenu,command=self.product, image=self.icon_side, compound=LEFT, text="Product", font=("times new roman", 18, "bold"), bg="white", cursor="hand2", bd=2, padx=5, anchor="w", height=40).pack(side=TOP,fill=X)
        btn_stock = Button(LeftMenu, command=self.stock,image=self.icon_side, compound=LEFT, text="Stock", font=("times new roman", 18, "bold"), bg="white", bd=2, cursor="hand2", padx=5, anchor="w", height=40).pack(side=TOP,fill=X)

        btn_sale= Button(LeftMenu, command=self.sale, image=self.icon_side, compound=LEFT, text="Sale", font=("times new roman", 18, "bold"), bg="white", bd=2, cursor="hand2", padx=5, anchor="w", height=40).pack(side=TOP,fill=X)
        btn_sold = Button(LeftMenu, command=self.sold, image=self.icon_side, compound=LEFT, text="Sold", font=("times new roman", 18, "bold"), bg="white", bd=2, cursor="hand2", padx=5, anchor="w", height=40).pack(side=TOP,fill=X)
        btn_exit = Button(LeftMenu, command=self.exit,image=self.icon_side, compound=LEFT, text="Exit", font=("times new roman", 18, "bold"), bg="white", bd=2, cursor="hand2", padx=5, anchor="w", height=40).pack(side=TOP,fill=X)

 

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4


    def sale(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = saleClass(self.new_win)

    def sold(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = soldClass(self.new_win)

    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)

    def stock(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = stockClass(self.new_win)

    def exit(self):
        exit=messagebox.askyesno("Exit", "Do you really want exit?", parent=self.root)
        if exit==True:
            self.root.destroy()

if __name__ =="__main__":
    os.system('python start.py')
    root = Tk()
    obj = IMS(root)
    root.mainloop()
    