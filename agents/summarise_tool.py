from .agents_base import AgentBase

class Summarise_Tool(AgentBase):
    def __init__(self, max_retries, verbose=True):
        super().__init__(name = "Summarise_Tool", max_retries=max_retries, verbose=verbose)
    
    def execute(self, text):
        messages = [
            {"role":"system","content":"You are an AI assistant that summarises Medical Texts."},
            {"role":"user","content":"Please provide a concise summary of the following medical texts:\n\n"
             f"{text}\n\nSummary:"}
        ]

        # summary = self.call_openai(messages, max_tokens=300)
        summary = self.call_llama(messages, max_tokens=300)
        return summary
