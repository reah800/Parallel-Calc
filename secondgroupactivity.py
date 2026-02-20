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

#pharmacist approval
pharmacist_lock = threading.Lock()

def pharmacist_approves():
    
    return random.random() < 0.8

def approve(pid):
    with pharmacist_lock:
        print(f"[{pid}] Pharmacist approval started")
        time.sleep(0.3)
        if pharmacist_approves():
            print(f"[{pid}] Approved and dispensed")
            return True
        else:
            print(f"[{pid}] Rejected — needs correction")
            return False

# Sequential execution
def fulfill_sequential(prescriptions):
    print("\n--- Sequential Execution ---")
    start = time.time()
    for pid in prescriptions:
        while True:
            intake(pid)
            verify(pid)
            retrieve(pid)
            label_and_package(pid)
            process_payment(pid)
            if approve(pid):
                break
            else:
                print(f"[{pid}] Reprocessing due to rejection...\n")
    end = time.time()
    return end - start

# Parallel execution
def process_prescription(pid):
    while True:
        intake(pid)
        verify(pid)
        retrieve(pid)
        label_and_package(pid)
        process_payment(pid)
        if approve(pid):
            break
        else:
            print(f"[{pid}] Reprocessing due to rejection...\n")

def fulfill_parallel(prescriptions):
    print("\n--- Parallel Execution ---")
    start = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(process_prescription, prescriptions)
    end = time.time()
    return end - start


# Run benchmark
if name == "main":
    prescriptions = [f"Rx-{i}" for i in range(1, 11)]

    seq_time = fulfill_sequential(prescriptions)
    par_time = fulfill_parallel(prescriptions)

    print(f"\nSequential Time: {seq_time:.2f} seconds")
    print(f"Parallel Time:   {par_time:.2f} seconds")
    print(f"Speedup:         {seq_time / par_time:.2f}x")