from tkinter import *

window = Tk()

window.geometry("400x470")
window.resizable(0, 0)
window.title("Pixel Calculator")

in_frame = Frame(window, width=380, height=50)
in_frame.pack(side=TOP)

b_frame = Frame(window, width=380, height=450, bg="Darkgrey")
b_frame.pack()


count_text = StringVar()
entry = Entry(in_frame, font=("Helvetica", 20, "bold"), textvariable=count_text, width=70, justify=RIGHT)
entry.grid(row=0, column=0)
entry.pack(ipady=14)

solution = ""
def button_click(label):
  global solution
  if label == "C":
    solution = ""
    count_text.set("")
  elif label == "=":
    result = str(eval(solution))
    count_text.set(result)
    solution = ""
  else:
    solution = solution + str(label)
    count_text.set(solution)

def create_button(parent, text, row, column, command, width=13, columnspan=1):
  btn = Button(
    parent,
    text=text,
    width=width,
    height=5,
    bd=0,
    bg="White" if text.isdigit() else "lightgrey",
    command=command
  )
  btn.grid(row=row, column=column, columnspan=columnspan, padx=1, pady=1)

create_button(b_frame, "C", 0,0, lambda: button_click("C"), width=42, columnspan=3)
create_button(b_frame, "0", 4,0, lambda: button_click(0), width=27, columnspan=2)
create_button(b_frame, ".", 4,2, lambda: button_click("."))

operations = ["/", "*", "+", "-", "="]
for i in range(len(operations)):
  op = operations[i]
  create_button(b_frame, op, i,3, lambda oper=op: button_click(oper))

for i in range(9):
  create_button(b_frame, str(i+1), i//3 + 1,i%3, lambda num=i+1: button_click(num))
  

window.mainloop()