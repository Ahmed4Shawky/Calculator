from tkinter import *
import ast

root = Tk()
root.title("Calculator")
root.geometry("380x400")
root.configure(bg="#1e1e1e")

i = 0

def get_number(num):
    global i
    display.insert(i, num)
    i += 1

def get_operations(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length    

def clear_all(event=None):
    display.delete(0, END)

def calculate(event=None):
    entire_string = display.get()
    try:
        node = ast.parse(entire_string, mode="eval")
        result = eval(compile(node, '<string>', 'eval'))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

def undo(event=None):
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "")

display = Entry(root, font=("Arial", 18), borderwidth=5, relief="sunken", justify="left", bg="#f0f0f0", fg="#000000")
display.grid(row=1, columnspan=6, padx=10, pady=10, ipady=10)

# Set focus to the display as soon as the app starts
display.focus_set()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0

# Number buttons
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = Button(root, text=button_text, width=4, height=2, font=("Arial", 14), fg="#ffffff", bg="#333333", command=lambda text=button_text: get_number(text))
        button.grid(row=x+2, column=y, padx=5, pady=5)
        counter += 1

button = Button(root, text=0, width=4, height=2, font=("Arial", 14), fg="#ffffff", bg="#333333", command=lambda: get_number(0))
button.grid(row=5, column=1, padx=5, pady=5)

count = 0
operations = ['+', '-', '*', '/', '*3.14', '%', '()', '**', ')', "**2"]

# Operation buttons
for x in range(4):
    for y in range(3):
        if count < len(operations):
            button = Button(root, text=operations[count], width=4, height=2, font=("Arial", 14), fg="#ffffff", bg="#555555", command=lambda text=operations[count]: get_operations(text))
            count += 1
            button.grid(row=x+2, column=y+3, padx=5, pady=5)

# Special Buttons
Button(root, text="AC", width=4, height=2, font=("Arial", 14), fg="#ffffff", bg="#e74c3c", command=clear_all).grid(row=5, column=0, padx=5, pady=5)
Button(root, text="=", width=4, height=2, font=("Arial", 14), fg="#ffffff", bg="#27ae60", command=calculate).grid(row=5, column=2, padx=5, pady=5)
Button(root, text="<-", width=4, height=2, font=("Arial", 14), fg="#ffffff", bg="#f39c12", command=undo).grid(row=5, column=4, padx=5, pady=5)

# Bind keyboard events
root.bind('<Return>', calculate)
root.bind('<BackSpace>', undo)
root.bind('<c>', clear_all)
root.bind('<C>', clear_all)
root.bind('<Delete>', clear_all)

root.mainloop()
