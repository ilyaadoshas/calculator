import customtkinter as ctk

ctk.set_default_color_theme("gray_theme.json")

class Calculator (ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("350x550")
        self.resizable(width=False,height=False)

        self.row_col()
        self.display()
        self.buttons()

    def row_col(self):
        self.columnconfigure((0,1,2,3),weight = 1,uniform="row")
        self.rowconfigure(0,weight=2)
        self.rowconfigure((1,2,3,4,5),weight=1,uniform="col")

    def display(self):
        self.display = ctk.CTkEntry(self, font=("robot", 50), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew",padx=3,pady=3)
    
    def buttons(self):
        labels = [
            ["C","(",")","÷"],
            ["7","8","9","x"],
            ["4","5","6","-"],
            ["1","2","3","+"],
            ["±","0",".","="]

        ]
        for r,row in enumerate(labels,start=1):
            for c,text in enumerate(row):
                btn = ctk.CTkButton(self,text=text,height=20,width=20,)
                btn.grid(row=r,column=c,sticky="nsew",padx=3,pady=3)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()