from customtkinter import *

set_default_color_theme("gray_theme.json")

root = CTk()
root.title("Calculator")
root.geometry("350x550")
root.resizable(width=False,height=False)




root.columnconfigure((0, 1, 2, 3), weight=1, uniform="col")
root.rowconfigure(0, weight=2)
root.rowconfigure((1, 2, 3, 4, 5), weight=1, uniform="row")

ntr = CTkEntry(root,height=150,width=350,font=("robot",60)).grid(row=0,column=0,columnspan=4,sticky="ew")

btn_div = CTkButton(root,text="÷",height=80,width=80,font=("robot",60)).grid(row=1,column=3,sticky="nsew")
btn_mult = CTkButton(root,text="x",height=80,width=80,font=("robot",60)).grid(row=2,column=3,sticky="nsew")
btn_plus = CTkButton(root,text="+",height=80,width=80,font=("robot",60)).grid(row=3,column=3,sticky="nsew")
btn_minus = CTkButton(root,text="-",height=80,width=80,font=("robot",60)).grid(row=4,column=3,sticky="nsew")
btn_eq = CTkButton(root,text="=",height=80,width=80,font=("robot",60)).grid(row=5,column=3,sticky="nsew")
btn_dot = CTkButton(root,text=".",height=80,width=80,font=("robot",60)).grid(row=5,column=2,sticky="nsew")
btn_0= CTkButton(root,text="0",height=80,width=80,font=("robot",60)).grid(row=5,column=1,sticky="nsew")
btn_con= CTkButton(root,text="±",height=80,width=80,font=("robot",60)).grid(row=5,column=0,sticky="nsew")
btn_1= CTkButton(root,text="1",height=80,width=80,font=("robot",60)).grid(row=4,column=0,sticky="nsew")
btn_2= CTkButton(root,text="2",height=80,width=80,font=("robot",60)).grid(row=4,column=1,sticky="nsew")
btn_3= CTkButton(root,text="3",height=80,width=80,font=("robot",60)).grid(row=4,column=2,sticky="nsew")
btn_4= CTkButton(root,text="4",height=80,width=80,font=("robot",60)).grid(row=3,column=0,sticky="nsew")
btn_5= CTkButton(root,text="5",height=80,width=80,font=("robot",60)).grid(row=3,column=1,sticky="nsew")
btn_6= CTkButton(root,text="6",height=80,width=80,font=("robot",60)).grid(row=3,column=2,sticky="nsew")
btn_7= CTkButton(root,text="7",height=80,width=80,font=("robot",60)).grid(row=2,column=0,sticky="nsew")
btn_8= CTkButton(root,text="8",height=80,width=80,font=("robot",60)).grid(row=2,column=1,sticky="nsew")
btn_9= CTkButton(root,text="9",height=80,width=80,font=("robot",60)).grid(row=2,column=2,sticky="nsew")
btn_C= CTkButton(root,text="C",height=80,width=80,font=("robot",60)).grid(row=1,column=0,sticky="nsew")
btn_p1= CTkButton(root,text="(",height=80,width=80,font=("robot",60)).grid(row=1,column=1,sticky="nsew")
btn_p2= CTkButton(root,text=")",height=80,width=80,font=("robot",60)).grid(row=1,column=2,sticky="nsew")


root.mainloop()