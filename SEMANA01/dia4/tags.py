import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_777=tk.Button(root)
        GButton_777["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_777["font"] = ft
        GButton_777["fg"] = "#000000"
        GButton_777["justify"] = "center"
        GButton_777["text"] = "Button"
        GButton_777.place(x=60,y=50,width=70,height=25)
        GButton_777["command"] = self.GButton_777_command

        GLineEdit_281=tk.Entry(root)
        GLineEdit_281["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_281["font"] = ft
        GLineEdit_281["fg"] = "#333333"
        GLineEdit_281["justify"] = "center"
        GLineEdit_281["text"] = "Entry"
        GLineEdit_281.place(x=140,y=50,width=70,height=25)

        GLabel_33=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_33["font"] = ft
        GLabel_33["fg"] = "#333333"
        GLabel_33["justify"] = "center"
        GLabel_33["text"] = "label"
        GLabel_33.place(x=240,y=50,width=70,height=25)

    def GButton_777_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
