from customtkinter import *

root = CTk()
root.title("Calculator")
root.geometry("350x550")

root.columnconfigure(0, weight=1000)
root.rowconfigure(0, weight=1)
root.columnconfigure((1,2,3,4), weight=1)
root.rowconfigure((1,2,3,4), weight=1)

label_1 = CTkLabel(root, text="0", bg_color="gray")
label_1.grid(row = 0 , column = 0 , sticky = "nswe")


root.mainloop()