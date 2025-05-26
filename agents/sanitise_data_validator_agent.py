from .agents_base import AgentBase

class Sanitise_Data_Validator_Agent(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(name = "Sanitise_Data_Validator_Agent", max_retries=max_retries, verbose=verbose)
    
    def execute(self, original_data, sanitized_data):
        system_message = "You are an expert AI AI assistant that validates the sanitizing of medical data by checking the removal of PHI"
        user_content = (
            "Given the original data and the sanitized data, verify that all PHI has been removed.\n"
            "List any remaining PHI in the sanitized data and rate the sanitization process on a scale of 1 to 5, where 5 indicates complete sanitization.\n\n"
            f"Original Data:\n{original_data}\n\n"
            f"Sanitized Data:\n{sanitized_data}\n\n"
            "Validation:"
        )

        messages = [
            {"role":"system", "content":system_message},
            {
                "role":"user", "content":user_content
            }
        ]

        # article = self.call_openai(messages, max_tokens=300)
        article = self.call_llama(messages, max_tokens=512)
        return article
