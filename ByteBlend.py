import tkinter as tk
import os
import customtkinter as ctk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
from datetime import datetime
from time import strftime


class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("400x300")
        self.configure(fg_color='#1a365d')
        self.wm_attributes('-fullscreen', True)
        self.logo = ctk.CTkImage(light_image=Image.open('Logo.png'), size=(450, 400))
        self.logo_label = ctk.CTkLabel(self, image=self.logo, text='')
        self.logo_label.place(x=0, y=0)

        self.username_entry = ctk.CTkEntry(self,text_color='black', font=("Comic Sans MS", 16), border_color='black', placeholder_text='Username', fg_color='white')
        self.password_entry = ctk.CTkEntry(self,text_color='black', show="*", font=("Comic Sans MS", 16), border_color='black', placeholder_text='Password', fg_color='white')
        self.login_button = ctk.CTkButton(self, text="Login", font=("Comic Sans MS", 16, 'bold'), fg_color='#90AFC7', width=100, height=1, corner_radius=0, command=self.check_login)
        self.username_entry.place(x=450, y=160)
        self.password_entry.place(x=450, y=200)
        self.login_button.place(x=467, y=240)
        self.mainloop()

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "valtugnez":
            self.destroy()
            App('ByteBlend', (1980, 1080))
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

class App(ctk.CTk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.config(bg='#81c3d7')
        self.wm_attributes('-fullscreen', True)
        self.geometry(f'{size[0]}x{size[1]}')
        self.frame1 = topFrame(self)
        self.frame2 = bottomFrame(self)
        self.frame3 = orderFrame(self)
        self.frame4 = TreeView(self)
        self.mainloop()
class topFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=1230, height=100, fg_color='#2b5d7c', bg_color='#2b5d7c')
        self.place(x=0, y=0)
        self.time_label = ctk.CTkLabel(self, text='', text_color='white', font=("Comic Sans MS", 20, 'bold'), width=200)
        self.time_label.place(relx=0.5, rely=0.5, anchor='center')
        self.labelValtugNez = ctk.CTkLabel(self, text='ValTugNez', text_color='white', font=("Comic Sans MS", 20, 'bold'))
        self.labelValtugNez.place(x=20, y=20)
        self.update_time()
    def update_time(self):
        current_time = datetime.now().strftime('%B %d %Y - %H:%M:%S')
        self.time_label.configure(text=current_time)
        self.after(1000, self.update_time) # #
class bottomFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=757, height=595, fg_color='#3a7ca5', bg_color='#3a7ca5')
        self.place(x=0, y=99)
        self.bottomfunctionCall()
        self.display = drink_button_frame(self)
    def bottomfunctionCall(self):
        self.crt_widgets()
        self.wdgt_lyt()
    def crt_widgets(self):
        self.drink_btn = ctk.CTkButton(self, text='Beverages', text_color='black', font=("Comic Sans MS", 21, 'bold'), fg_color='transparent', height=100, corner_radius=0, command=self.drink_button_frame)
        self.food_btn = ctk.CTkButton(self, text='Foods', text_color='black', font=("Comic Sans MS", 20, 'bold'), fg_color='transparent', height=100, corner_radius=0, command=self.food_button_frame)
        self.mix_btn = ctk.CTkButton(self, text='Mix&Match', text_color='black', font=("Comic Sans MS", 20, 'bold'), fg_color='transparent', height=100, corner_radius=0, command=self.mix_button_frame)
    def wdgt_lyt(self):
        self.drink_btn.place(x=107, y=500)
        self.food_btn.place(x=258, y=500)
        self.mix_btn.place(x=427, y=500)
    def drink_button_frame(self):
        drink_button_frame(self)
    def food_button_frame(self):
        food_button_frame(self)
    def mix_button_frame(self):
        mix_button_frame(self)
class TreeView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=757, height=501, fg_color='#81C3D7', corner_radius=0)
        self.place(x=817, y=241)
        self.table()

    def table(self):
        global tree
        tree = ttk.Treeview(self, columns=('Name', 'Quantity', 'Price'), show='headings', selectmode='browse', height=13)
        tree.heading('Name', text='Name', )
        tree.heading('Quantity', text='Quantity')
        tree.heading('Price', text='Price')
        tree.column('Name', width=120, minwidth=120)
        tree.column('Quantity', width=120, minwidth=120)
        tree.column('Price', width=120, minwidth=120)
        tree.pack()

    def insert_item(self, name, quantity, price, category):
        tree.insert('', 'end', values=(name, quantity, price, category))

class orderFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=472, height=595, fg_color='white', corner_radius=0)
        self.place(x=757, y=100)
        self.orderFunctionCall()
        self.connection = mysql.connector.connect(host='localhost', user='root', password='', database='byteblend_database')
        self.sql = self.connection.cursor()
        self.frame4 = TreeView(self)
    def orderFunctionCall(self):
        self.crt_wdgts()
        self.wdgt_lyt()
    def crt_wdgts(self):
        self.pay_button = ctk.CTkButton(self, text='Pay', font=("Comic Sans MS", 35, 'bold'), fg_color='#90AFC7', width=477, height=100, corner_radius=0)
        self.total_bill_lbl = ctk.CTkLabel(self, text='Total Bill', text_color='white', font=("Comic Sans MS", 25, 'bold'), fg_color='#90AFC7', width=90, height=30, corner_radius=0, padx=200, pady=6)
        self.total_price_lbl1 = ctk.CTkLabel(self, text='Total Price (PHP):', text_color='black', font=("Comic Sans MS", 20, 'bold'))
        self.total_price_lbl2 = ctk.CTkLabel(self, text="PHP 0.00", text_color='black', font=("Comic Sans MS", 20, 'bold'), width=100, padx=5)
        self.Delete_button = ctk.CTkButton(self, text='Remove',  font=("Comic Sans MS", 20, 'bold'), fg_color='#90AFC7', hover_color='red', width=100, corner_radius=0, command=None)
        self.Update_button = ctk.CTkButton(self, text='Update',  font=("Comic Sans MS", 20, 'bold'), fg_color='#90AFC7', width=120, corner_radius=0, command=None)
        self.Clear_button = ctk.CTkButton(self, text='Cancel',  font=("Comic Sans MS", 20, 'bold'), fg_color='#90AFC7', hover_color='red', width=100, corner_radius=0, command=self.cancel_order)
        self.Search_button = ctk.CTkEntry(self, text_color='white', placeholder_text_color='white', placeholder_text='Search...', fg_color='#90AFC7', border_color='white')

    def wdgt_lyt(self):
        self.pay_button.place(x=0, y=499)
        self.total_bill_lbl.place(x=0, y=0)
        self.total_price_lbl1.place(x=10, y=457)
        self.total_price_lbl2.place(x=335, y=457)
        self.Delete_button.place(x=360, y=60)
        self.Update_button.place(x=179, y=60)
        self.Clear_button.place(x=15, y=60)
        self.Search_button.place(x=170, y=103)

    def cancel_order(self):
        delete_query = 'DELETE FROM cafe_data'
        self.sql.execute(delete_query)
        self.connection.commit()
        tree.delete(*tree.get_children())
class drink_button_frame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=757, height=501, fg_color='#81C3D7', corner_radius=0)
        self.place(x=0, y=0)
        self.connection = mysql.connector.connect(host='localhost', user='root', password='', database='byteblend_database')
        self.sql = self.connection.cursor()
        self.drinkFunctionCall()
        self.frame4 = TreeView(self)
        global file_path
    def drinkFunctionCall(self):
        self.drink_crt_wdgt()
        self.drink_wdgt_lyt()

    def add_to_treeview(self, name, quantity, price, category):
        insert_query = 'INSERT into cafe_data (Name, Quantity, Price, Category) VALUES (%s, %s, %s, %s)'
        values = (name, quantity, price, category)
        self.sql.execute(insert_query, values)
        self.connection.commit()
        self.frame4.insert_item(name, quantity, price, category)
    def drink_crt_wdgt(self):
        file_path = os.path.dirname(os.path.realpath(__file__))
        self.drink_lbl = ctk.CTkLabel(self, text='Beverages', font=("Comic Sans MS", 20, 'bold'))
        self.pictures1 = ctk.CTkImage(Image.open(file_path + "/Beverages/Americano.png"), size=(70, 70))
        self.pictures2 = ctk.CTkImage(Image.open(file_path + "/Beverages/Cream Latte.png"), size=(70, 70))
        self.pictures3 = ctk.CTkImage(Image.open(file_path + "/Beverages/Espresso.png"), size=(70, 70))
        self.pictures4 = ctk.CTkImage(Image.open(file_path + "/Beverages/Flat White.png"), size=(70, 70))
        self.pictures5 = ctk.CTkImage(Image.open(file_path + "/Beverages/Macchiato.png"), size=(70, 70))
        self.pictures6 = ctk.CTkImage(Image.open(file_path + "/Beverages/Mocha.png"), size=(70, 70))
        self.pictures7 = ctk.CTkImage(Image.open(file_path + "/Beverages/Black Coffee.png"), size=(70, 70))
        self.pictures8 = ctk.CTkImage(Image.open(file_path + "/Beverages/Coup de grace.png"), size=(70, 70))
        self.pictures9 = ctk.CTkImage(Image.open(file_path + "/Beverages/Chateau.png"), size=(70, 70))
        self.menu1 = ctk.CTkButton(self, image=self.pictures1, text='Americano PHP 150', text_color='black',font=("Comic Sans MS", 12, 'bold'), fg_color='white', compound='top', width=165,height=120, corner_radius=27, command=lambda: self.add_to_treeview('Americano', 1, 150, 'Beverages'))
        self.menu2 = ctk.CTkButton(self, image=self.pictures2, text='Creamy Latte PHP 150', text_color='black', font=("Comic Sans MS", 10, 'bold'), fg_color='white', compound='top', width=165, height=120, corner_radius=27, command=lambda: self.add_to_treeview('Creamy Latte', 1, 150, 'Beverages'))
        self.menu3 = ctk.CTkButton(self, image=self.pictures3, text='Espresso PHP 150', text_color='black', font=("Comic Sans MS", 12, 'bold'), fg_color='white', compound='top', width=165, height=120, corner_radius=27, command=lambda: self.add_to_treeview('Espresso', 1, 150, 'Beverages'))
        self.menu4 = ctk.CTkButton(self, image=self.pictures4, text='Flat White PHP 150', text_color='black', font=("Comic Sans MS", 12, 'bold'), fg_color='white', compound='top', width=165, height=120, corner_radius=27, command=lambda: self.add_to_treeview('Flat White', 1, 150, 'Beverages'))
        self.menu5 = ctk.CTkButton(self, image=self.pictures5, text='Macchiato PHP 150', text_color='black', font=("Comic Sans MS", 12, 'bold'), fg_color='white', compound='top', width=165, height=120, corner_radius=27, command=lambda: self.add_to_treeview('Macchiato', 1, 150, 'Beverages'))
        self.menu6 = ctk.CTkButton(self, image=self.pictures6, text='Mocha PHP 150', text_color='black', font=("Comic Sans MS", 12, 'bold'), fg_color='white', compound='top', width=165, height=120, corner_radius=27, command=lambda: self.add_to_treeview('Mocha', 1, 150, 'Beverages'))
        self.menu7 = ctk.CTkButton(self, image=self.pictures7, text='Black Coffee PHP 150', text_color='black', font=("Comic Sans MS", 10, 'bold'), fg_color='white', compound='top', width=165, height=120, corner_radius=27, command=lambda: self.add_to_treeview('Black Coffee', 1, 150, 'Beverages'))
        self.menu8 = ctk.CTkButton(self, image=self.pictures8, text='Coup De Grace PHP 150', text_color='black', font=("Comic Sans MS", 8, 'bold'), fg_color='white', compound='top', width=165, height=120, corner_radius=27, command=lambda: self.add_to_treeview('Coup De Grace', 1, 150, 'Beverages'))
        self.menu9 = ctk.CTkButton(self, image=self.pictures9, text='Chateau PHP 150', text_color='black', font=("Comic Sans MS", 12, 'bold'), fg_color='white', compound='top', width=165, height=120, corner_radius=27, command=lambda: self.add_to_treeview('Chateau', 1, 150, 'Beverages'))

    def drink_wdgt_lyt(self):
        self.drink_lbl.place(x=80, y=20)
        self.menu1.place(x=70, y=70)
        self.menu2.place(x=70, y=200)
        self.menu3.place(x=70, y=330)
        self.menu4.place(x=270, y=70)
        self.menu5.place(x=270, y=200)
        self.menu6.place(x=270, y=330)
        self.menu7.place(x=470, y=70)
        self.menu8.place(x=470, y=200)
        self.menu9.place(x=470, y=330)




class food_button_frame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=757, height=501, fg_color='#81C3D7', corner_radius=0)
        self.place(x=0, y=0)
        self.foodFunctionCall()
        self.connection = mysql.connector.connect(host='localhost', user='root', password='', database='byteblend_database')
        self.sql = self.connection.cursor()
        self.frame4 = TreeView(self)
    def foodFunctionCall(self):
        self.food_crt_wdgt()
        self.food_wdgt_lyt()

    def add_to_treeview(self, name, quantity, price, category):
        insert_query = 'INSERT into cafe_data (Name, Quantity, Price, Category) VALUES (%s, %s, %s, %s)'
        values = (name, quantity, price, category)
        self.sql.execute(insert_query, values)
        self.connection.commit()
        self.frame4.insert_item(name, quantity, price, category)

    def food_crt_wdgt(self):
        file_path = os.path.dirname(os.path.realpath(__file__))
        self.drink_lbl = ctk.CTkLabel(self, text='Foods', font=("Comic Sans MS", 20, 'bold'))
        self.pictures1 = ctk.CTkImage(Image.open(file_path + "/Foods/Bread Saandwich.png"), size=(70, 70))
        self.pictures2 = ctk.CTkImage(Image.open(file_path + "/Foods/Cheese Pie.png"), size=(70, 70))
        self.pictures3 = ctk.CTkImage(Image.open(file_path + "/Foods/Egg pie.png"), size=(70, 70))
        self.pictures4 = ctk.CTkImage(Image.open(file_path + "/Foods/Pretzels.png"), size=(70, 70))
        self.pictures5 = ctk.CTkImage(Image.open(file_path + "/Foods/Slice Pizza.png"), size=(70, 70))
        self.pictures6 = ctk.CTkImage(Image.open(file_path + "/Foods/Vanila cake.png"), size=(70, 70))
        self.pictures7 = ctk.CTkImage(Image.open(file_path + "/Foods/Croissant.png"), size=(70, 70))
        self.pictures8 = ctk.CTkImage(Image.open(file_path + "/Foods/Cream Donut.png"), size=(70, 70))
        self.pictures9 = ctk.CTkImage(Image.open(file_path + "/Foods/Slice of Strawberry Cake.png"), size=(70, 70))
        self.menu1 = ctk.CTkButton(self, image=self.pictures1, text='Sandwich PHP 105', text_color='black', font=("Comic Sans MS", 13, 'bold'), fg_color='white', compound='top', width=165, height=120, corner_radius=27)
        self.menu2 = ctk.CTkButton(self, image=self.pictures2, text='Cheese Pie PHP 95', text_color='black', font=("Comic Sans MS", 12, 'bold'), fg_color='white', compound='top', height=120, corner_radius=27)
        self.menu3 = ctk.CTkButton(self, image=self.pictures3, text='Egg Pie PHP 130', text_color='black', font=("Comic Sans MS", 13, 'bold'), fg_color='white', compound='top', width=165, height=120, corner_radius=27)
        self.menu4 = ctk.CTkButton(self, image=self.pictures4, text='Pretzels PHP 20', text_color='black', font=("Comic Sans MS", 13, 'bold'), fg_color='white', compound='top', width=165, height=120, corner_radius=27)
        self.menu5 = ctk.CTkButton(self, image=self.pictures5, text='SlicePizza PHP 60', text_color='black', font=("Comic Sans MS", 13, 'bold'), fg_color='white', compound='top', width=165, height=120, corner_radius=27)
        self.menu6 = ctk.CTkButton(self, image=self.pictures6, text='Cake PHP 250', text_color='black', font=("Comic Sans MS", 13, 'bold'), fg_color='white', compound='top', width=165, height=120, corner_radius=27)
        self.menu7 = ctk.CTkButton(self, image=self.pictures7, text='Croissant PHP 175', text_color='black', font=("Comic Sans MS", 10, 'bold'), fg_color='white', compound='top', width=165, height=120, corner_radius=27)
        self.menu8 = ctk.CTkButton(self, image=self.pictures8, text='Cream Donut PHP 180', text_color='black',font=("Comic Sans MS", 10, 'bold'), fg_color='white', compound='top', width=165, height=120, corner_radius=27)
        self.menu9 = ctk.CTkButton(self, image=self.pictures9, text='Berry Cake PHP 250', text_color='black', font=("Comic Sans MS", 10, 'bold'), fg_color='white', compound='top', width=165, height=120, corner_radius=27)

    def food_wdgt_lyt(self):
        self.drink_lbl.place(x=80, y=20)
        self.menu1.place(x=70, y=70)
        self.menu2.place(x=70, y=200)
        self.menu3.place(x=70, y=330)
        self.menu4.place(x=270, y=70)
        self.menu5.place(x=270, y=200)
        self.menu6.place(x=270, y=330)
        self.menu7.place(x=470, y=70)
        self.menu8.place(x=470, y=200)
        self.menu9.place(x=470, y=330)
class mix_button_frame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=757, height=501, fg_color='#81C3D7', corner_radius=0)
        self.place(x=0, y=0)
        self.mixFunctionCall()

    def mixFunctionCall(self):
        self.mix_crt_wdgt()
        self.mix_wdgt_lyt()

    def mix_crt_wdgt(self):
        file_path = os.path.dirname(os.path.realpath(__file__))
        self.drink_lbl = ctk.CTkLabel(self, text='Mix&Match', font=(None, 20, 'bold'))
        self.pictures1 = ctk.CTkImage(Image.open(file_path + "/Mix&Match/Emoji 1.png"), size=(100, 100))
        self.pictures2 = ctk.CTkImage(Image.open(file_path + "/Mix&Match/Emoji 2.png"), size=(100, 100))
        self.pictures3 = ctk.CTkImage(Image.open(file_path + "/Mix&Match/Emoji 3.png"), size=(100, 100))
        self.pictures4 = ctk.CTkImage(Image.open(file_path + "/Mix&Match/Emoji 4.png"), size=(100, 100))
        self.pictures5 = ctk.CTkImage(Image.open(file_path + "/Mix&Match/Emoji 5.png"), size=(100, 100))
        self.pictures6 = ctk.CTkImage(Image.open(file_path + "/Mix&Match/Emoji 6.png"), size=(100, 100))
        self.pictures7 = ctk.CTkImage(Image.open(file_path + "/Mix&Match/Emoji 7.png"), size=(100, 100))
        self.pictures8 = ctk.CTkImage(Image.open(file_path + "/Mix&Match/Emoji 8.png"), size=(100, 100))
        self.pictures9 = ctk.CTkImage(Image.open(file_path + "/Mix&Match/Emoji 9.png"), size=(70, 70))
        self.menu1 = ctk.CTkButton(self, image=self.pictures1, text='', text_color='black', font=("Comic Sans MS", 13, 'bold'), fg_color='white', compound='top', width=165, height=120, corner_radius=27)
        self.menu2 = ctk.CTkButton(self, image=self.pictures2, text='', text_color='black', font=("Comic Sans MS", 12, 'bold'), fg_color='white', compound='top', height=120, corner_radius=27)
        self.menu3 = ctk.CTkButton(self, image=self.pictures3, text='', text_color='black', font=("Comic Sans MS", 13, 'bold'), fg_color='white', compound='top', width=165, height=120, corner_radius=27)
        self.menu4 = ctk.CTkButton(self, image=self.pictures4, text='', text_color='black', font=("Comic Sans MS", 13, 'bold'), fg_color='white', compound='top', width=165, height=120, corner_radius=27)
        self.menu5 = ctk.CTkButton(self, image=self.pictures5, text='', text_color='black', font=("Comic Sans MS", 13, 'bold'), fg_color='white', compound='top', width=165, height=120, corner_radius=27)
        self.menu6 = ctk.CTkButton(self, image=self.pictures6, text='', text_color='black', font=("Comic Sans MS", 13, 'bold'), fg_color='white', compound='top', width=165, height=120, corner_radius=27)
        self.menu7 = ctk.CTkButton(self, image=self.pictures7, text='', text_color='black',font=("Comic Sans MS", 10, 'bold'), fg_color='white', compound='top', width=165, height=120, corner_radius=27)
        self.menu8 = ctk.CTkButton(self, image=self.pictures8, text='', text_color='black',  font=("Comic Sans MS", 10, 'bold'), fg_color='white', compound='top', width=165,  height=120, corner_radius=27)
        self.menu9 = ctk.CTkButton(self, image=self.pictures9, text='', text_color='black', font=("Comic Sans MS", 10, 'bold'), fg_color='white', compound='top', width=165, height=120, corner_radius=27)
    def mix_wdgt_lyt(self):
        self.drink_lbl.place(x=80, y=20)
        self.menu1.place(x=70, y=70)
        self.menu2.place(x=70, y=200)
        self.menu3.place(x=70, y=330)
        self.menu4.place(x=270, y=70)
        self.menu5.place(x=270, y=200)
        self.menu6.place(x=270, y=330)
        self.menu7.place(x=470, y=70)
        self.menu8.place(x=470, y=200)
        self.menu9.place(x=470, y=330)


LoginWindow()
