import tkinter as tk
from tkinter import ttk
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

# (Task Parallelism)
def compute_sss(salary): return salary * 0.045
def compute_philhealth(salary): return salary * 0.025
def compute_pagibig(salary): return salary * 0.02
def compute_tax(salary): return salary * 0.10

# (Data Parallelism)
employees = [
    ("Alice", 25000),
    ("Bob", 32000),
    ("Charlie", 28000),
    ("Diana", 40000),
    ("Edward", 35000)
]

# Payroll computation function
def compute_payroll(employee):
    name, salary = employee
    sss = compute_sss(salary)
    philhealth = compute_philhealth(salary)
    pagibig = compute_pagibig(salary)
    tax = compute_tax(salary)
    total_deduction = sss + philhealth + pagibig + tax
    net_salary = salary - total_deduction
    return (name, salary, total_deduction, net_salary)

