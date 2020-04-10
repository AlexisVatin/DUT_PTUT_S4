import tkinter as tk
import sqlite3
import time
from logic.bot_form import Bot


class TradBox(tk.Tk):


    def __init__(self, root, french_word, translated_word):
        super(TradBox, self).__init__()
        self.title = 'translate'
        self.db = sqlite3.connect('translate.db')
        # self.top = tk.Toplevel(self.root)

        frm = tk.Frame(self, borderwidth=4, relief='ridge')
        frm.pack(fill='both', expand=True)

        self.label = tk.Label(frm, text="French word : " + french_word)
        self.label.pack(padx=4, pady=4)
        self.input = tk.Entry(frm)
        self.input.insert(0, french_word)
        self.input.config(state="disabled")
        self.input.pack()

        # Input mot à traduire
        self.label_name = tk.Label(frm, text="Input translation")
        self.input_name = tk.Entry(frm)
        self.input_name.insert(0, translated_word)
        self.label_name.pack()
        self.input_name.pack()

        self.btn_add_to_form = tk.Button(frm, text="Submit to Form", command=self.execForm)
        self.btn_add_to_form.pack()

        self.btn_add_name = tk.Button(frm, text="Submit", command=self.add_to_db)
        self.btn_add_name.pack()
        b_cancel = tk.Button(frm, text='Cancel')
        b_cancel['command'] = self.destroy
        b_cancel.pack(padx=4, pady=4)

    def add_to_db(self):
        c = self.db.cursor()
        query = '''INSERT INTO word(word, trad_anglais) VALUES (?,?)'''
        c.execute(query, (self.input.get(), self.input_name.get()))
        self.db.commit()

    def execForm(self):
        Bot().execForm(self.input.get(), self.input_name.get())


