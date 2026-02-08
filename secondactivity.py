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