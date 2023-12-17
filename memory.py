import sys
sys.path.append('../../')

import json
import datetime

from filefuncs import *

class MemoryTree:
	def __init__(self, mem_file): 
		# Base information about the agent.
	    self.name = None
	    self.first_name = None
	    self.last_name = None
	    self.age = None
	    # permanent core traits.  
	    self.innate = None

	    self.currently = None
	    self.lifestyle = None
	    self.living_area = None

	    # Personal plans
	    self.daily_req = []

	    # WORLD INFORMATION
	    # Perceived world time. 
	    self.curr_time = None
	    # Daily average plans
	    self.daily_plan_req = []
	    if check_if_file_exists(mem_file): 
	      # If we have a bootstrap file, load that here. 
	      scratch_load = json.load(open(mem_file))
	      #TODO load mem data from file