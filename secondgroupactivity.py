import time
import threading
import random
from concurrent.futures import ThreadPoolExecutor

# Simulated task 
def intake(pid):
    print(f"[{pid}] Intake started")
    time.sleep(0.5)
    print(f"[{pid}] Intake completed")

def verify(pid):
    print(f"[{pid}] Verification started")
    time.sleep(0.7)
    print(f"[{pid}] Verification completed")

def retrieve(pid):
    print(f"[{pid}] Retrieval started")
    time.sleep(0.6)
    print(f"[{pid}] Retrieval completed")

def label_and_package(pid):
    print(f"[{pid}] Packaging started")
    time.sleep(0.4)
    print(f"[{pid}] Packaging completed")

def process_payment(pid):
    print(f"[{pid}] Payment processing started")
    time.sleep(0.5)
    print(f"[{pid}] Payment completed")


