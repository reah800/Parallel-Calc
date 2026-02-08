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