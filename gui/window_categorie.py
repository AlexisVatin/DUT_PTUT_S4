# import tkinter as tk
#
#
# class window_categorie(tk.Frame):
#     def __init__(self):
#         super(window_categorie, self).__init__()
#         self.title = 'modify'
#         self.name_list = tk.Listbox(selectmode=tk.SINGLE)
#
#
#         # Close
#         self.btn_quit = tk.Button(self, text="Quit", command=self.quit_app)
#
#
#
#         # Place element on main window
#
#         self.name_list.pack()
#         self.btn_quit.pack()
#
#
#
#
#     # def add_name_to_list(self):
#     #     name = self.input_name.get()
#     #     if name:
#     #         c = self.db.cursor()
#     #         query = '''INSERT INTO name(name) VALUES (?)'''
#     #         c.execute(query, [name])
#     #         self.db.commit()
#     #         self.name_list.insert(0, [name])
#     #
#     # def remove_name_from_list(self):
#     #     index = self.name_list.curselection()
#     #     if len(index):
#     #         name = self.name_list.get(index)[0]
#     #         c = self.db.cursor()
#     #         query = '''DELETE FROM name WHERE name=?'''
#     #         c.execute(query, [name])
#     #         self.db.commit()
#     #         self.name_list.delete(index)
#
#     # def run_bot(self):
#     #     list_name = reversed(self.name_list.get(0, self.name_list.size()))
#     #     bot = Bot(list_name, "drivers\chromedriver.exe",  self.input_num_loop.get())
#     #     bot.execute()
#
#     def quit_app(self):
#         self.db.close()
#         self.destroy()
#
