from .agents_base import AgentBase

class Write_Article_Validator_Agent(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(name = "Write_Article_Validator_Agent", max_retries=max_retries, verbose=verbose)
    
    def execute(self, topic, article):
        system_message = "You are an expert AI assistance that validates research articles"
        user_content = (
            "Given the topic and the article, assess whether the article comprehensively covers the topic, follows a logical structure, and maintains academic standards.\n"
            "Provide a brief analysis and rate the article on a scale of 1 to 5, where 5 indicates excellent quality.\n\n"
            f"Topic: {topic}\n\n"
            f"Article:\n{article}\n\n"
            "Validation:"
        )

        messages = [
            {"role":"system", "content":system_message},
            {
                "role":"user", "content":user_content
            }
        ]

        # article = self.call_openai(messages, max_tokens=300)
        validation = self.call_llama(messages, max_tokens=512)
        return validation
