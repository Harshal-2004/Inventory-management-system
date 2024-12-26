from sqlite3.dbapi2 import Cursor, connect
from tkinter import *
from tkinter.font import BOLD  
from PIL import ImageTk
import PIL.Image
from tkinter import ttk, messagebox
import sqlite3

class soldClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1055x485+205+127")
        self.root.title("Sold | IMS ")
        self.root.config(bg="white")
        photo = PhotoImage(file = "images\i1.png")
        self.root.iconphoto(False, photo)
        self.root.focus_force()
        self.root.resizable(False, False)
        #root.overrideredirect(1)

        #########################################

       
        self.var_pid =StringVar()
        self.var_sup =StringVar()
        self.var_name =StringVar()
        self.var_price =StringVar()
        self.var_qty =StringVar()
        self.var_brd =StringVar()

        #---Title--
        title = Label(root, text="SOLD PRODUCT DETAILS", font=("goudy old style", 15, "bold"), bg="IndianRed4", fg="white").pack(side=TOP,fill=X)


   
        #===Product details===

        p_frame = Frame(self.root, bd=3, relief=RIDGE)
        p_frame.place(x=80,y=30,width=900, height=450)

        scrolly = Scrollbar(p_frame, orient= VERTICAL)
        scrollx = Scrollbar(p_frame, orient= HORIZONTAL)



        self.product_table = ttk.Treeview(p_frame, columns=("pid","Supplier", "name", "price", "qty" ,"brd"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)

        self.product_table.heading("pid", text="Product ID")    
        self.product_table.heading("Supplier", text="Supplier")  
        self.product_table.heading("name", text="Name")
        self.product_table.heading("price", text="Price")
        self.product_table.heading("qty", text="Quantity")
        self.product_table.heading("brd", text="BRAND")
        self.product_table["show"] = "headings"

        self.product_table.column("pid", width=90)
        self.product_table.column("Supplier", width=100)        
        self.product_table.column("name", width=100)
        self.product_table.column("price", width=100)
        self.product_table.column("qty", width=100)
        self.product_table.column("brd", width=100)
        self.product_table.pack(expand=1, fill=BOTH)
        self.product_table.bind("<ButtonRelease-1>", self.get_data)

        self.show()



##########################################################################################################################################

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from sales")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        self.var_pid.set(row[0])       
        self.var_sup.set(row[1])
        self.var_name.set(row[2])
        self.var_price.set(row[3])
        self.var_qty.set(row[4])
        self.var_brd.set(row[5])
 


if __name__ =="__main__":
    root = Tk()
    obj = soldClass(root)
    root.mainloop()