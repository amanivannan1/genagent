import math
import sys
import datetime
import random
sys.path.append('../')

from filefuncs import *
from memory import *

class Agent: 
  def __init__(self, name, memfile):
    
    # <name> is a unique identifier for Agent
    self.name = name

    # PERSONA MEMORY 
    f_s_mem_saved = f"{memfile}"
    self.s_mem = MemoryTree(f_s_mem_saved)
   