#!/usr/bin/python

import Tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.initialize()
        
    def initialize(self):
        pass
        
if __name__ == "__main__":
    app = Application(None)
    app.master.title("Test")
    app.mainloop()
