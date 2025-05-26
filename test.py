import ollama

response = ollama.chat(model='llama3.2:latest', messages=[{'role': 'user', 'content': 'Hi'}])
print(response['message']['content'])