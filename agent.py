import math
import sys
import datetime
import random
sys.path.append('../')

from filefuncs import *

class Agent: 
  def __init__(self, name, bio, memfile):
    
    # <name> is a unique identifier for Agent
    self.name = name
    # <bio> is the initial Natural language statement description of the agent
    self.bio = bio

    # PERSONA MEMORY 
    f_s_mem_saved = f"{memfile}"
    self.s_mem = MemoryTree(f_s_mem_saved)
   