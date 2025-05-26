from .summarise_tool import Summarise_Tool
from .write_article_tool import Write_Article_Tool
from .sanitise_data_tool import Sanitise_Data_Tool
from .summary_validator_agent import Summarise_Validator_Agent
from .write_article_validator_agent import Write_Article_Validator_Agent
from .sanitise_data_validator_agent import Sanitise_Data_Validator_Agent
from .refiner_agent import Refiner_Tool
from .validator_agent import Validator_Agent

class Agent_Manager():
    def __init__(self, max_retries=2, verbose=True):
        self.agents = {
        "summarise":Summarise_Tool(max_retries=max_retries, verbose=verbose),
        "write_Article":Write_Article_Tool(max_retries=max_retries, verbose=verbose),
        "sanitise_Data":Sanitise_Data_Tool(max_retries=max_retries, verbose=verbose),
        "summarise_validator":Summarise_Validator_Agent(max_retries=max_retries, verbose=verbose),
        "write_article_validator": Write_Article_Validator_Agent(max_retries=max_retries, verbose=verbose),
        "sanitise_data_validator": Sanitise_Data_Validator_Agent(max_retries=max_retries, verbose=verbose),
        "refiner": Refiner_Tool(max_retries=max_retries, verbose=verbose),      # New agent
        "validator": Validator_Agent(max_retries=max_retries, verbose=verbose)   # New agent

        }
    def get_agent(self, agents_name):
        agent = self.agents.get(agents_name)
        if not agent:
            raise ValueError(f"Agent '{agents_name}' not Found.")
        return agent


