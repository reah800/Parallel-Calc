4. Your group should answer the following questions in a README.md or separate file in your repository: 
      1. Which approach demonstrates true parallelism in Python? Explain.
      Since each process in Python operates independently on different CPU cores, multiprocessing provides real parallelism, whereas multithreading is constrained by the Global Interpreter Lock.

      2. Compare execution times between multithreading and multiprocessing.
      Multithreading was faster than multiprocessing. The multithreading run finished in about 0.036 seconds, while multiprocessing took around 0.199 seconds. Threads are lighter and share memory, so they have less overhead, while processes achieve true parallelism but are slower here because of the extra startup cost.


      3. Can Python handle true parallelism using threads? Why or why not?
      Python cannot handle true parallelism using threads for CPU-bound tasks. It can only achieve concurrency (sharing one core by switching back and forth) due to the GIL (Global Interpreter Lock). True parallelism is only achieved via multiprocessing.

      4. What happens if you input a large number of grades (e.g., 1000)? Which
      method is faster and why?  
      With a large number of grades, multiprocessing is faster because it uses multiple CPU cores for true parallelism, while multithreading slows down due to the Global Interpreter Lock and thread management overhead.

      5. Which method is better for CPU-bound tasks and which for I/O-bound Tasks?
      Multiprocessing is better for CPU-bound tasks because it can use multiple CPU cores, however multithreading on the other hand is better for tasks that wait for input or output like reading files or getting data from the internet. With this, Multithreading is better for I/O bound tasks.

      6. How did your group apply creative coding or algorithmic solutions in this Lab?
      Our group applied creative coding by designing a colorful GUI, adding a results table with execution times, and implementing both multithreading and multiprocessing algorithms to compare performance, making the program interactive, robust, and visually engaging.

-------------------------------Third Laboratory Activity - Applying Task and Data Parallelism using concurrent.futures--------------------------------

Provide concise but well-structured explanations.
1) Differentiate Task and Data Parallelism. Identify which part of the lab
demonstrates each and justify the workload division.

 The difference between dask parallelism and data parallelism is that for PART A, task parallelism uses ThreadPoolExecutor, meaning that it is implemented as a separate function per deduction type. The functions run concurrently but operate on the same salary value, thus the workload is divided by type of task. for part B however data parallelism, it uses ProcessPoolExecutor, thus this means that Data parallelism happens when the same operation is applied to multiple data elements in parallel. A single payroll computation function is applied to multiple employees concurrently; furthermore, the workload is divided by data elements which are the employees.

2) Explain how concurrent.futures managed execution, including submit(),
map(), and Future objects. Discuss the purpose of with when creating an
Executor.

 Concurrent.futures module manages concurrent execution through providing executor that handles worker threads or processes for us.  With this, the executor automatically takes care of scheduling and running tasks.

 Submit () method is used to schedule a function to run asynchronously and returns a future object. 

 map() applies a function to multiple inputs concurrently and returns results in order.

 future  represents a result that may not yet be completed, tsuch as calling .result() blocks until the tasks finishes.

 The purpose of submit() in the part a was to execute different deduction functions, while map() in part B was used to apply the payroll function to all employees.


3) Analyze ThreadPoolExecutor execution in relation to the GIL and CPU cores. Did
true parallelism occur? No, true parallelism did not occur in  ThreadPoolExecutor.

Python's Global Interpreter Lock (GIL) allows only one thread to execute Python bytecode at a time within a single process. 
Even though ThreadPoolExecutor creates multiple threads, the GIL serializes their execution, meaning only one deduction function runs at any given instant.
In our output, we can observe that all tasks were executed by the same thread pool worker (`ThreadPoolExecutor-0_0`), indicating sequential execution within the thread pool.


4) Explain why ProcessPoolExecutor enables true parallelism?
      `ProcessPoolExecutor` enables true parallelism** in our `run_data_parallelism()` function because it spawns separate OS-level processes:


            "with ProcessPoolExecutor() as executor:"
                  "results = executor.map(compute_payroll, employees)"


Each of the five `compute_payroll` calls runs in its own process. This achieves true parallelism for three key reasons:

1. **Independent GILs** — Each worker process has its own Python interpreter with its own GIL. This means multiple processes can execute Python bytecode *truly simultaneously* on different CPU cores. Unlike `ThreadPoolExecutor`, there is no single lock blocking concurrent execution.

2. **Separate memory spaces** — Each process operates in its own memory space. The `employees` list and the `compute_payroll` function are serialized (pickled) and sent to each worker. The returned tuples `(name, salary, total_deduction, net_salary)` are pickled back to the main process. This isolation prevents shared-state race conditions but adds serialization overhead.

3. **Multi-core utilization** — The OS scheduler distributes worker processes across available CPU cores. With 5 employees and (for example) 4+ cores, up to 4 or 5 payroll calculations happen simultaneously.



5) Evaluate scalability if the system increases from 5 to 10,000 employees. Which
approach scales better and why?

If the system grows from 5 to 10,000 employees, Data Parallelism scales much better because it can run the same payroll computation for many employees at the same time across multiple CPU cores. Using ProcessPoolExecutor, each process can handle different employees independently, which makes the system faster and more efficient than using Task Parallelism for a large number of employees.

6) Provide a real-world payroll system example. Indicate where Task Parallelism and
Data Parallelism would be applied, and which executor you would use.

Data Parallelism would be applied, and which executor you would use.
In a real payroll system, Task Parallelism can be used to calculate differences for a single employee at the same time, such as SSS, PhilHealth, Pag-IBIG, and withholding tax, using ThreadPoolExecutor. On the other hand, Data Parallelism can be used to compute salaries for many employees at once, applying the same payroll calculation function to each employee using ProcessPoolExecutor. This way, the system can handle both single -employee tasks and large -scale employee processing efficiently. 


                         Third Laboratory Activity - Applying Task and Data Parallelism using concurrent.futures
