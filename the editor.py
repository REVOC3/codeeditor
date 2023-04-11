import tkinter as tk
import tkinter.ttk as ttk
import os

class CodeEditor(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('800x1200')
        self.title('Code Editor')
        self.resizable(0, 0)
        self.background('#dedede')
        # Creating a toolbar
        toolbar = ttk.Toolbar(self)
        toolbar.grid(column=0, row=0, sticky='ns')
        self.register(toolbar)

        # Creating a menu bar
        menu = ttk.Menu(self)
        self.config(menu=menu)
        file_menu = ttk.Menu(menu)
        menu.add_cascade(label='File', menu=file_menu)
        edit_menu = ttk.Menu(menu)
        menu.add_cascade(label='Edit', menu=edit_menu)
        save_menu = ttk.Menu(edit_menu)
        quit_menu = ttk.Menu(edit_menu)
        save_menu.add_command(label='Save')
        save_menu.add_command(label='Save As')
        quit_menu.add_command(label='E&xit')

        # Creating some buttons
        browse_button = ttk.Button(self)
        browse_button['text'] = 'Browse...'
        browse_button['command'] = self.open_file_dialog

        # Creating a scrollbar
        self.text = tk.Text(self)
        self.text.grid(row=0, column=1)
        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.text.yview)
        self.scrollbar.grid(column=1, row=0, sticky='ns')
