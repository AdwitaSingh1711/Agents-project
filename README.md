# Multi-Agent AI System 🤖

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/Ollama-4A4A4A?style=for-the-badge)](https://ollama.ai/)

A collaborative multi-agent system powered by local LLMs, featuring dynamic conversation management and task-oriented agent specialization.

![Agent System Architecture](https://via.placeholder.com/800x400.png?text=System+Architecture+Diagram)

## Features ✨

- **Multi-Model Support**: Seamlessly switch between OpenAI API and local Ollama models
- **Agent Specialization**: Role-specific agents (research, refining, validating)
- **Local Model Support**: Run private models via Ollama

## Installation 🛠️

### Prerequisites
- Python 3.9+
- Ollama (for local models)

```bash
# Clone repository
git clone https://github.com/your-username/agents.git
cd agents

# Set up virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install Ollama (macOS)
brew install ollama

# Start Ollama service
ollama serve &

# Pull desired model (e.g., llama3)
ollama pull llama3
