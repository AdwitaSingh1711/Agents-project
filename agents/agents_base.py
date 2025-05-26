# import openai
import ollama
from abc import ABC, abstractmethod
from loguru import logger
import os
from dotenv import load_dotenv

load_dotenv()

# openai.api_key = os.getenv('OPEN_AI_API_KEY')

class AgentBase(ABC):
    def __init__(self, name, max_retries=2, verbose=True):
        self.name = name
        self.max_retries = max_retries
        self.verbose = verbose
    
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    def call_llama(self, messages, temperature = 0.7, max_tokens = 150):
        retries=0
        while retries < self.max_retries:
            try:
                if self.verbose:
                    logger.info(f"[{self.name}] Sending message to OPEN AI")
                    for msg in messages:
                        logger.debug(f"{msg['role']}: {msg['content']}")
                
                response = ollama.chat(
                    model = 'llama3.2:latest',
                    messages = messages,
                    # temperature=temperature,
                    # max_tokens = max_tokens
                )

                # reply = response.choices[0].message
                reply = response['message']['content']
                if self.verbose:
                    logger.info(f"[{self.name}] Received response {reply}")
                
                return reply
            
            except Exception as e:
                retries+=1
                logger.error(f"[{self.name}] Error during OpenAI call: {e}. Retry {retries}/{self.max_retries}")
        
        raise Exception(f"[{self.name}] Failed to get response from LLama after {self.max_retries} retries.")