from .agents_base import AgentBase

class Summarise_Validator_Agent(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(name = "Summarise_Validator_Agent", max_retries=max_retries, verbose=verbose)
    
    def execute(self, original_text, summary):
        system_message = "You are an expert AI assistant that validates the summaries of medical texts"
        user_content = (
            "Given the original summary, assess whether the summary accurately captures the key points and is of high quality \n"
            "Provide a brief analysis and rate the summary on a scale of 1 to 5, where 5 indicates excellent quality.\n\n"
            f"Topic: {original_text}\n\n"
            f"Article:\n{summary}\n\n"
            "Validation:"
        )

        messages = [
            {"role":"system", "content":system_message},
            {
                "role":"user", "content":user_content
            }
        ]

        # validation = self.call_openai(messages, max_tokens=300)
        validation = self.call_llama(messages, max_tokens=512)
        return validation
