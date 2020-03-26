# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from console_ui import ConsoleUi
import signal

class App(ttk.Frame):

  def __init__(self, root):
    super().__init__()
    self.root = root
    root.title("Factory Test")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    self.init_UI()
    self.bind_event()

  def init_UI(self):
    self.pack(fill=tk.BOTH, expand=True)

    # frame1
    frame1 = ttk.Frame(self)
    frame1.pack(fill=tk.X)
    lbl_sn = ttk.Label(frame1, text="Serial Number")
    lbl_sn.pack(side=tk.LEFT)

    self.entry_sn = ttk.Entry(frame1)
    self.entry_sn.pack(fill=tk.X)

    # frame2
    frame2 = ttk.Frame(self)
    frame2.pack(fill=tk.X)
    self.btn_test = ttk.Button(frame2, text="Test", command=self.on_click)
    self.btn_test.pack(fill=tk.X)

    # frame3
    frame3 = ttk.Frame(self)
    frame3.pack(fill=tk.BOTH, expand=True)
    frame3.columnconfigure(0, weight=1)
    frame3.rowconfigure(0, weight=1)

    self.console = ConsoleUi(frame3)
    self.console.pack(fill=tk.BOTH, expand=False)

  def bind_event(self):
    self.root.protocol('WM_DELETE_WINDOW', self.quit)
    self.root.bind('<Control-q>', self.quit)
    signal.signal(signal.SIGINT, self.quit)


  # EVENT
  def quit(self, *args):
    self.root.destroy()

  def on_click(self):
    self.console.log('HELLOHELLO')
    self.console.log_e('WORRRRRRRRRRRD')

def main():
  root = tk.Tk()
  app = App(root)
  app.root.mainloop()

if __name__ == '__main__':
  main()
