import tkinter as tk

def press(key):
    global expression
    expression += str(key)

display_var.set(expression)

def clear():
    global expression
    expression= "" display_var.set("")