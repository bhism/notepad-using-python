import os
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfile, asksaveasfile, askopenfilename, asksaveasfilename


def newFile():
    global file
    root.title("untitled - note")
    file= None
    TextArea.delete(1.0,END)
def openFile():
    global file

    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),
                                                              ("Text Documents","*.txt")])
    if file == "":
        file=None
    else:
        root.title(os.path.basename(file)+"- note")
        TextArea.delete(1.0,END)
        f =open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()
        root.title(os.path.basename(file)+"- note")
        print("File Saved")


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="untitled.txt",defaultextension=".txt",
                                 filetypes=[("All Files","*.*"),("Text Document","*.txt")])
        if file =="":
            file=None
        else:
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
    else:
        # save current open file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
def quitApp():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("made by","bhism (Webfun)")




if __name__ =='__main__':
    # basic tkinter setup
    root =Tk()
    root.title("untitled")
    root.wm_iconbitmap("___.png")
    root.geometry("644x688")
    # textarea
    TextArea =Text(root,font="lucida 13")
    file = None
    TextArea.pack(expand =True ,fill = BOTH)
    # menubar
    MenuBar =Menu(root)
    # file menu start
    FileMenu = Menu(MenuBar , tearoff = 0)
    # to open new file
    FileMenu.add_command(label="new" , command =newFile)
    # to open already existing file
    FileMenu.add_command(label="open" , command =openFile)
    # to save current file
    FileMenu.add_command(label="save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label = "File",menu = FileMenu)
    # file menu ends

    # edit menu start
    EditMenu = Menu(MenuBar,tearoff = 0)
    # to give a feature of cut,copy and paste
    EditMenu.add_command(label = "Cut", command = cut)
    EditMenu.add_command(label = "Copy", command = copy)
    EditMenu.add_command(label = "Paste", command = paste)

    MenuBar.add_cascade(label="Edit", menu =EditMenu)
    # edit menu end

    # help menu start
    HelpMenu = Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label ="about notepad", command =about)
    MenuBar.add_cascade(label="Help" , menu = HelpMenu)
    # help menu end
    root.config(menu = MenuBar)

    # adding scroll bar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command = TextArea.yview)
    TextArea.config(yscrollcommand = Scroll.set)
    root.mainloop()
