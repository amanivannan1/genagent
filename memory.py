import sys
sys.path.append('../../')

import json
import datetime

from filefuncs import *

class MemoryTree:
    def __init__(self, mem_file): 
        # Base information about the agent.
        self.name = None
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
        self.past_action_summary = None
        self.act_address = None
        self.act_duration = None
        self.act_description = None
        if check_if_file_exists(mem_file): 
          # If we have a bootstrap file, load that here. 
          load_mem = json.load(open(mem_file))
          
          self.name = load_mem["name"]
          self.age = load_mem["age"]
          self.innate = load_mem["innate"]
          self.currently = load_mem["currently"]
          self.lifestyle = load_mem["lifestyle"]
          self.living_area = load_mem["living_area"]
          self.daily_req = load_mem["daily_req"]
          self.curr_time = load_mem["curr_time"]
          self.daily_plan_req = load_mem["daily_plan_req"]
          self.past_action_summary = load_mem["past_action_summary"]
          self.act_address = load_mem["act_address"]
          self.act_duration = load_mem["act_duration"]
          self.act_description = load_mem["act_description"]

    def save(self, mem_file):
        mem = dict()
        load_mem["name"] = self.name
        load_mem["age"] = self.age
        load_mem["innate"] = self.innate
        load_mem["currently"] = self.currently
        load_mem["lifestyle"] = self.lifestyle
        load_mem["living_area"] = self.living_area
        load_mem["curr_time"] = self.curr_time.strftime("%B %d, %Y, %H:%M:%S")
        load_mem["daily_plan_req"] = self.daily_plan_req
        load_mem["past_action_summary"] = self.past_action_summary
        load_mem["act_address"] = self.act_address
        load_mem["act_duration"] = self.act_duration
        load_mem["act_description"] = self.act_description
          