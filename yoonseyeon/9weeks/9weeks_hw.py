from tkinter import *

window = Tk()

window.title("냥이들^^")
photo1 = PhotoImage(file= r"C:\Users\jooro\OneDrive\바탕 화면\PythonProgramming_\Week9\cat1.gif")
photo2 = PhotoImage(file= r"C:\Users\jooro\OneDrive\바탕 화면\PythonProgramming_\Week9\cat2.gif")

label1 = Label(window, image = photo1)
label2 = Label(window, image = photo2)

label1.pack(side=LEFT)
label2.pack(side=LEFT)

window.mainloop()