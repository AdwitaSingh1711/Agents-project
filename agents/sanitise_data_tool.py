from .agents_base import AgentBase

class Sanitise_Data_Tool(AgentBase):
    def __init__(self, max_retries, verbose=True):
        super().__init__(name = "Sanitise_Data_Tool", max_retries=max_retries, verbose=verbose)
    
    def execute(self, medical_data):
        messages = [
            {"role":"system","content":"You are an AI assistant that sanitises Medical Data by removing Protected Health Information (PHI)."},
            {"role":"user","content":"Remove all PHI from the following data:\n\n"
             f"{medical_data}\n\nSanitised Data:"}
        ]

        # sanitised_data = self.call_openai(messages, max_tokens=300)
        sanitised_data = self.call_llama(messages, max_tokens=500)
        return sanitised_data
