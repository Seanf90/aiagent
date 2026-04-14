# AI Agent (CLI)

A command-line AI agent powered by Google's Gemini API, capable of autonomously reading, modifying, and running Python code.

## What it does
- Accepts a natural language instruction via the command line
- Reads relevant Python files from the working directory
- Plans and applies code changes using the Gemini API
- Executes the modified code and reports the result
- Iterates until the task is complete

## Why this is interesting
This project implements a basic **agentic loop** a pattern increasingly used in production AI systems, where an LLM is given tools and autonomously decides how to use them to complete a goal.

## Tech
- Python
- Google Gemini API
- File system I/O and subprocess execution

## How to run
```bash
git clone https://github.com/Seanf90/aiagent
cd aiagent
pip install -r requirements.txt
```
Add your Gemini API key to a `.env` file:
GEMINI_API_KEY=your_key_here
Then run:
```bash
python main.py "your instruction here"
```
