from tkinter import Tk
from ui.gui import GUI

def gui():
    window = Tk()
    window.title("Storage manager")

    program = GUI(window)
    program.start()

    window.mainloop()

if __name__ == "__main__":
    gui()
