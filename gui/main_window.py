import tkinter as tk
import sqlite3
from gui import dialog
from logic import api_trad
from config import yandex_API, url_Yandex
from logic.bot_form import Bot


class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.title = 'translate'
        self.db = sqlite3.connect('translate.db')
        # self.create_table()

        # Run
        self.btn_run = tk.Button(self, text="Run", command=self.run_bot)

        # List name
        self.name_list = tk.Listbox(selectmode=tk.SINGLE)

        self.insert_all_word()

        # Input mot à traduire
        self.frame_name = tk.Frame(self)
        self.label_name = tk.Label(self.frame_name, text="Input word")
        self.input_name = tk.Entry(self.frame_name, text="Get")

        # Add / Delete
        self.frame_btn = tk.Frame(self)
        self.btn_add_name = tk.Button(self.frame_btn, text="Add word", command=self.add_name_to_list)
        self.btn_remove_name = tk.Button(self.frame_btn, text="Delete word", command=self.remove_name_from_list)

        # Close
        self.btn_quit = tk.Button(self, text="Quit", command=self.quit_app)

        # Place element on main window

        self.btn_run.pack()
        self.name_list.pack()

        self.label_name.grid(row=0, column=0)
        self.input_name.grid(row=0, column=1)
        self.frame_name.pack()

        self.btn_add_name.grid(row=0, column=0)
        self.btn_remove_name.grid(row=0, column=1)
        self.frame_btn.pack()

        self.btn_quit.pack()

    def add_name_to_list(self):
        translated_word = api_trad.translate(url_Yandex, yandex_API, self.input_name.get())
        trad_box = dialog.TradBox(self, self.input_name.get(), translated_word)

    def remove_name_from_list(self):
        index = self.name_list.curselection()
        if len(index):
            name = self.name_list.get(index)
            name = name.split(" : ")
            name = name[0]

            c = self.db.cursor()
            query = '''DELETE FROM word WHERE word=?'''
            c.execute(query, [name])
            self.db.commit()
            self.name_list.delete(index)
        self.name_list.delete(0, tk.END)
        self.insert_all_word()

    def insert_all_word(self):
        c = self.db.cursor()
        c.execute('''SELECT * FROM word''')
        rows = c.fetchall()
        for row in rows:
            self.name_list.insert(0, row[1] + " : " + row[2])

    def quit_app(self):
        self.db.close()
        self.destroy()

    def run_bot(self):
        Bot().execute()
