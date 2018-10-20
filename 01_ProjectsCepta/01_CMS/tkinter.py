import TKinter
from TKinter import*
root = Tk()
root.minsize(300,300)
mainMenu = Menu(root)

fileSubMenu = Menu(mainMenu)
mainMenu.add_cascade(label="open")
mainMenu.add_cascade(label="Save")


mainMenu.add_command(lable="File")
mainMenu.add_command(lable="Edit")
mainMenu.add_command(lable="View")

root.config(menu=mainMenu)








root.mainloop()