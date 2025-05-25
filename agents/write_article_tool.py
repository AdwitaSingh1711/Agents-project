from .agents_base import AgentBase

class Write_Article_Tool(AgentBase):
    def __init__(self, max_retries, verbose=True):
        super().__init__(name = "Write_Article_Tool(", max_retries=max_retries, verbose=verbose)
    
    def execute(self, topic, outline=None):
        system_message = "You are an expert academic writer."
        user_content = f"write a research article on the follwoing topic: \nTopic:{topic}\n\n"

        if outline:
            user_content +=f"Outline:\n{outline}\n\n"
        user_content += "Article:\n"

        messages = [
            {"role":"system", "content":system_message},
            {
                "role":"user", "content":user_content
            }
        ]

        article = self.call_openai(messages, max_tokens=300)
        return article
