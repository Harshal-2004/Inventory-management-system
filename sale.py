from sqlite3.dbapi2 import Cursor, connect
from tkinter import *
from tkinter.font import BOLD  
from PIL import ImageTk
import PIL.Image
from tkinter import ttk, messagebox
import sqlite3

class saleClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1055x485+205+127")
        self.root.title("Sales | IMS ")
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


        #---Frame---
        product_Frame=Frame(self.root, bd=2, relief=RIDGE, bg="white")
        product_Frame.place(x=10,y=10,width=450,height=465)
        
        #---Title--
        title = Label(product_Frame, text="Manage Sale Details", font=("goudy old style", 15, "bold"), bg="IndianRed4", fg="white").pack(side=TOP,fill=X)

        #---colum1---

        lbl_pid = Label(product_Frame, text=" Product ID", font=("goudy old style", 15), bg="white").place(x=30,y=60)
        lbl_supplier = Label(product_Frame, text="Supplier Name ", font=("goudy old style", 15), bg="white").place(x=30,y=110)
        lbl_product = Label(product_Frame, text=" Product Name", font=("goudy old style", 15), bg="white").place(x=30,y=160)
        lbl_price = Label(product_Frame, text=" Product Price", font=("goudy old style", 15), bg="white").place(x=30,y=210)
        lbl_qty = Label(product_Frame, text="Quantity", font=("goudy old style", 15), bg="white").place(x=30,y=260)
        lbl_brd = Label(product_Frame, text=" Product Brand", font=("goudy old style", 15), bg="white").place(x=30,y=310)

        #-----------
        txt_pid= Entry(product_Frame, textvariable=self.var_pid, font=("goudy old style", 15), bg="azure2")
        txt_pid.place(x=180, y=60, width=200)

        txt_sup = Entry(product_Frame, textvariable=self.var_sup, font=("goudy old style", 15), bg="azure2")
        txt_sup.place(x=180, y=110, width=200)

        txt_name = Entry(product_Frame, textvariable=self.var_name, font=("goudy old style", 15), bg="azure2")
        txt_name.place(x=180, y=160, width=200)

        txt_price = Entry(product_Frame, textvariable=self.var_price, font=("goudy old style", 15), bg="azure2")
        txt_price.place(x=180, y=210, width=200)

        txt_qty = Entry(product_Frame, textvariable=self.var_qty, font=("goudy old style", 15), bg="azure2")
        txt_qty.place(x=180, y=260, width=200)  


        txt_brd = Entry(product_Frame, textvariable=self.var_brd, font=("goudy old style", 15), bg="azure2")
        txt_brd.place(x=180, y=310, width=200)


        btn_add = Button(product_Frame, command=self.add, cursor="hand2", text="ADD TO SELL", font=("goudy old style", 15), bg="cyan4", fg="white").place(x=9,y=400,width=150, height=40)
        btn_delete = Button(product_Frame, command=self.delete, cursor="hand2", text="SELL", font=("goudy old style", 15), bg="red2", fg="white").place(x=227,y=400,width=100, height=40)


        #===Product details===

        p_frame = Frame(self.root, bd=3, relief=RIDGE)
        p_frame.place(x=470,y=20,width=575, height=450)

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
##########################################################################################################################################


    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if  self.var_sup.get()=="" or self.var_name.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("Select * from sales where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Product already present, try different", parent=self.root)
                else:
                    cur.execute("Insert into sales( pid , Supplier, name, price, qty , brd) values(?,?,?,?,?,?)", (
					self.var_pid.get(),
                                        self.var_sup.get(),                                        
                                        self.var_name.get(),
                                        self.var_price.get(),
                                        self.var_qty.get(),
                                        self.var_brd.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Product sold Added ", parent=self.root)
                    self.show()
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

 
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from product")
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
 


    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error", "Select product from the list", parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to SELL?", parent=self.root)
                    if op==True:
                        cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("SELL", "Product sell Successfully", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.var_pid.get(),
        self.var_sup.set(""),
        self.var_name.set(""),
        self.var_price.set(""),
        self.var_qty.set(""),
        self.var_brd.set("")

        self.show()


if __name__ =="__main__":
    root = Tk()
    obj = saleClass(root)
    root.mainloop()