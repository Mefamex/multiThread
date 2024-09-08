# -*- coding: utf-8 -*-
# Created on Sunday, September 08 10:00:00 2024
# @author: mefamex
# Github-repo: https://github.com/Mefamex/multiThread
# author-website: https://mefamex.com


import threading
from queue import Queue
from time import time,sleep
from random import randint

class POOL:
    """
    A thread pool for efficient parallel task execution.

    Args:
        max_threads (int, optional): Maximum number of threads in the pool. Defaults to 10.
        logFuture (bool, optional): Whether to store task results in a list. Defaults to True.
        ResultwhenDone (bool, optional): Whether to print task results immediately after completion. Defaults to False.
    """

    def __init__(self, max_threads:int=10, logFuture:bool=True, ResultwhenDone:bool=False):
        self.ResultwhenDone, self.logFuture =ResultwhenDone, logFuture
        self.task_queue, self.lock = Queue(), threading.Lock()
        self.futures , self.max_threads= [], max_threads
        self.start_time,self.task_times = None, []

    def _worker(self):
        """Worker function executed by each thread in the pool."""
        while True:
            func, args, kwargs = self.task_queue.get()
            task_start_time = time()
            try:
                result = func(*args, **kwargs)
                self.task_times.append( time() - task_start_time)
                if self.logFuture: self.futures.append(result)
                if self.ResultwhenDone: print(result)
            finally:self.task_queue.task_done()

    def submit(self, func, *args, **kwargs):
        """Submits a new task for execution.

        Args:
            func: The function to be executed.
            *args: Positional arguments for the function.
            **kwargs: Keyword arguments for the function.
        """
        if not self.start_time:self.start_time = time()
        self.task_queue.put((func, args, kwargs))
        with self.lock:
            if self.task_queue.qsize() > 0 and threading.active_count() < self.max_threads:
                threading.Thread(target=self._worker).start()

    def join(self):
        """Waits for all tasks to complete and returns results.

        Returns:
            tuple: A tuple containing the list of task results, elapsed time, and total time.
        """
        self.task_queue.join()
        elapsed_time = time() - self.start_time
        total_time = sum( [q for q in self.task_times ])
        
        print(f"Toplam geçen süre: {elapsed_time:.2f} saniye\n kurtarılan :{total_time-elapsed_time:.2f}")
        return self.futures,elapsed_time,total_time
      
