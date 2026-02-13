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





=============================================================================================================================================================================

                         Third Laboratory Activity - Applying Task and Data Parallelism using concurrent.futures