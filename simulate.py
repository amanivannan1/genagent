import math
import sys
import datetime
import random
sys.path.append('../')
from openai import OpenAI
from filefuncs import *
from agent import *
from dotenv import load_dotenv

# Setup client
load_dotenv()
client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

def main(): 
    # Create agent and initialize first summary
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
    agent.summary = completion.choices[0].message.content

    # Run memory loop
    memory_loop(agent)
  
def memory_loop(agent):
    # Summarize agent
    # Input user action
    # Reflect every 2 minutes
    # Update summary

    # Run 100 iterations
    for i in range(100):
        if i % 2 == 0:
            print("Agent Summary:")
            print(agent.summary)
            print("-------------")
        print("Current Action:")
        print(agent.s_mem.currently+"\n")
        user_action = input(agent.name+" should: \n")
        plan = agent.name + " should " + user_action+" now."
        query = "In one sentence, what is "+agent.name+" probably doing right now?"
        completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": agent.summary+"\n"+agent.s_mem.currently+"\n"+plan+"\n"+query
                }
            ],
            model="gpt-3.5-turbo",
        )
        agent.s_mem.currently = completion.choices[0].message.content
        completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": agent.summary+"\n"+agent.s_mem.currently+"\n"+"Give a brief summary of "+agent.name
                }
            ],
            model="gpt-3.5-turbo",
        )
        agent.summary = completion.choices[0].message.content
        print("-----hour: "+str(i)+"------\n")





if __name__=="__main__": 
    main() 