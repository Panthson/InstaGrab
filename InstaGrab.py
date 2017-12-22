import tkinter
import InstaGui as gui

def main():
    window = tkinter.Tk()
    window.resizable(width=False, height=False)
    download = gui.InstaGui(window)
    window.mainloop()

if __name__ == '__main__':
    main()
