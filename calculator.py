import tkinter as tk

def press(key):
    global expression
    expression += str(key)

display_var.set(expression)

def clear():
    global expression
    expression= "" display_var.set("")

    def erase():
    global expression
    expression = expression[:-1]
    display_var.set(expression)

def calculate():
    global expression
    try:
        result = str(eval(expression))
        display_var.set(result)
        expression = result
    except:
        display_var.set("Error")
        expression = ""


root = tk.Tk()
root.title("Calculator")
root.geometry("300x500")
root.configure(bg="#ffffff")
root.resizable(False, False)

expression = ""
display_var = tk.StringVar()
