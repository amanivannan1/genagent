import math
import sys
import datetime
import random
sys.path.append('../')
from openai import OpenAI
from filefuncs import *
from agent import *
from dotenv import load_dotenv


def main(): 
    load_dotenv()
    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
    )
    agent = Agent("Van Winkle", "agent1_mem.json")
    completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": agent.name + "is" + agent.s_mem.age + "and is " + agent.s_mem.innate + ". " + agent.s_mem.lifestyle 
                + " Give a summary of " + agent.name
            }
        ],
        model="gpt-3.5-turbo",
    )
    print( completion.choices[0].message.content)
  
def memory_loop():
    return

if __name__=="__main__": 
    main() 