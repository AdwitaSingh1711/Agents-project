from .agents_base import AgentBase

class Refiner_Tool(AgentBase):
    def __init__(self, max_retries, verbose):
        super().__init__(name="Refiner_Agent", max_retries=max_retries, verbose=verbose)

    def execute(self, draft):
        messages = [
            {"role":"system","content":
             [
                 {
                     "type":"text",
                    "text":"You are ana expert editor who refines and enhances articles for clarity, coherence "
                    "and academic importance."
                 }
             ]},
             {
                 "role":"user",
                 "content":[
                     {
                         "type":"text",
                         "text":"Please refine the following article draft to improve it's language, coherence"
                         "and overall quality. Think step-by-step.\n\n" 
                         f"{draft}\n\nRefinedArticle:"
                     }
                 ]
             }
        ]

        refined_article = self.call_openai(messages, temperature=0.3, max_tokens=1024)
        return refined_article