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