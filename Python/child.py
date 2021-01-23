"""
    This is the child process
"""
from multiprocessing import shared_memory
import numpy as np
import array

child = shared_memory.SharedMemory('data', False)

buffer = child.buf
data_list = list(buffer[:5])
print(data_list)
child.close()
