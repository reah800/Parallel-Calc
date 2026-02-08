import threading
from multiprocessing import Process, Queue
import time
import tkinter as tk
from tkinter import ttk, messagebox

def compute_gwa(grades):
    return sum(grades) / len(grades)

def thread_worker(grades, queue):
    gwa = compute_gwa(grades)
    queue.put(gwa)

def process_worker(grades, queue):
    gwa = compute_gwa(grades)
    queue.put(gwa)

def run_multithreading(grades, tree, progress):
    start = time.time()
    queue = Queue()
    threads = []

    for grade in grades:
        t = threading.Thread(target=thread_worker, args=([grade], queue))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    results = []
    while not queue.empty():
        results.append(queue.get())

    end = time.time()
    overall_gwa = compute_gwa(grades)

    tree.insert("", "end", values=("Multithreading", results, f"{overall_gwa:.2f}", f"{end - start:.6f}s"))
    progress.stop()
    progress['value'] = 100

def run_multiprocessing(grades, tree, progress):
    start = time.time()
    queue = Queue()
    processes = []

    for grade in grades:
        p = Process(target=process_worker, args=([grade], queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    results = []
    while not queue.empty():
        results.append(queue.get())

    end = time.time()
    overall_gwa = compute_gwa(grades)

    tree.insert("", "end", values=("Multiprocessing", results, f"{overall_gwa:.2f}", f"{end - start:.6f}s"))
    progress.stop()
    progress['value'] = 100

    # ---------- GUI Runner ----------
def run_method(method, entry, tree, progress):
    try:
        grades = [int(x) for x in entry.get().split()]
        if not grades:
            raise ValueError("No grades entered")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integer grades separated by spaces.")
        return

    progress['value'] = 0
    progress.start()

    if method == "thread":
        threading.Thread(target=lambda: run_multithreading(grades, tree, progress)).start()
    elif method == "process":
        threading.Thread(target=lambda: run_multiprocessing(grades, tree, progress)).start()

#Main Entry Point 
if __name__== "__main__":
    root = tk.Tk()
    root.title("Grade Computing System")

    tk.Label(root, text="Enter grades (separated by space):", bg="#e9afef", fg ="darkviolet").pack(pady=5)
    grades_entry = tk.Entry(root, width=40)
    grades_entry.pack(pady=5)

    progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="indeterminate")
    progress.pack(pady=10)

    columns = ("Method", "GWA Outputs", "Overall GWA", "Execution Time")
    tree = ttk.Treeview(root, columns=columns, show="headings", height=5,)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)
    tree.pack(pady=10)

    tk.Button(root, text="Run Multithreading", fg="darkviolet", command=lambda: run_method("thread", grades_entry, tree, progress)).pack(pady=5)
    tk.Button(root, text="Run Multiprocessing", fg="darkviolet", command=lambda: run_method("process", grades_entry, tree, progress)).pack(pady=5)

    root.configure(bg="#e9afef")

    root.mainloop()