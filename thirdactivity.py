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

# GUI Functions
def run_task_parallelism():
    # Example: run for Alice(Task Parallelism)
    name, salary = employees[0]  
    tasks = [compute_sss, compute_philhealth, compute_pagibig, compute_tax]
    results = []
    output_text.delete("1.0", tk.END) 

    output_text.insert(tk.END, f"Task Parallelism for {name} (Salary: {salary:.2f})\n\n")

    with ThreadPoolExecutor() as executor:
        future_to_task = {executor.submit(task, salary): task.__name__ for task in tasks}
        for future in as_completed(future_to_task):
            deduction = future.result()
            results.append(deduction)
            output_text.insert(tk.END, f"{future_to_task[future]}: {deduction:.2f}\n")

    total_deduction = sum(results)
    net_salary = salary - total_deduction

    output_text.insert(tk.END, f"\nTotal Deduction for {name}: {total_deduction:.2f}\n")
    output_text.insert(tk.END, f"Net Salary for {name}: {net_salary:.2f}\n")


def run_data_parallelism():
    output_text.delete("1.0", tk.END)  

    
    for row in tree.get_children():
        tree.delete(row)

    with ProcessPoolExecutor() as executor:
        results = executor.map(compute_payroll, employees)

    for name, gross, deduction, net in results:
        
        tree.insert("", tk.END, values=(name, f"{gross:.2f}", f"{deduction:.2f}", f"{net:.2f}"))
    
# GUI Runner 
if __name__== "__main__":
    root = tk.Tk()
    root.title("Payroll Parallelism System")

    tk.Label(root, text="Payroll Parallelism System", bg="#be9d80", fg ="#482700").pack(pady=5)
   
    output_text = tk.Text(root, width=60, height=20)
    output_text.pack(pady=5)
    tk.Button(root, text="Run Task Parallelism", bg="#694820", fg="#D4CABD", command=run_task_parallelism, width=25).pack(pady=5)
    tk.Button(root, text="Run Data Parallelism", bg="#694820", fg="#D4CABD", command=run_data_parallelism, width=25).pack(pady=5)

    # Treeview for Data Parallelism 
    columns = ("Employee", "Gross Salary", "Total Deduction", "Net Salary")
    tree = ttk.Treeview(root, columns=columns, show="headings", height=5)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)
    tree.pack(pady=10)

    root.configure(bg="#be9d80")

    root.mainloop()