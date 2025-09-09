# Ice-Breaker

Social media profile analyzer

## Overview

Ice-Breaker is a Python web application that analyzes public social media profiles (such as LinkedIn and Twitter/X) and generates a concise summary and interesting facts about a person. It is designed to help you break the ice in professional or social settings by providing quick, AI-generated insights based on publicly available information.

## Features

- **LinkedIn and Twitter/X Profile Lookup:**  
  Finds and analyzes public profiles using search and scraping APIs.

- **AI-Powered Summaries:**  
  Uses large language models to generate a short summary and two interesting facts about the person.

- **Profile Picture Retrieval:**  
  Attempts to fetch and display the person's profile picture.

- **Web Interface:**  
  Simple Flask-based web UI for entering a name and viewing results.

## Project Structure

```
ice_breaker/
├── agents/
│   └── ...                # Agent logic for profile lookup
├── third_parties/
│   └── linkedin.py        # LinkedIn scraping logic
├── tools/
│   └── tools.py           # Search and utility functions
├── templates/
│   └── index.html         # Web UI template
├── __init__.py
├── ...
app.py                     # Flask app entrypoint
main.py                    # Main orchestration logic
output_parsers.py          # Output parsing and formatting
requirements.txt           # Python dependencies (if present)
Pipfile                    # Pipenv dependencies
pyproject.toml             # Project metadata
README.md                  # This file
```

## Setup

### 1. Clone the repository

```sh
git clone <repo-url>
cd Ice-Breaker
```

### 2. Install dependencies

Using Pipenv (recommended):

```sh
pipenv install
pipenv shell
```

Or using pip:

```sh
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the project root with your API keys:

```
OPENAI_API_KEY=your-openai-key
SCRAPIN_API_KEY=your-scrapin-key
ZYTE_API_KEY=your-zyte-key
TAVILY_API_KEY=your-tavily-key
```

### 4. Run the application

```sh
python app.py
```

The app will be available at [http://localhost:5000](http://localhost:5000).

You can open it in your browser with:

```sh
$BROWSER http://localhost:5000
```

## Usage

1. Enter a person's name in the web form.
2. The app will search for their public LinkedIn and Twitter/X profiles.
3. It will display a summary, interesting facts, and (if available) a profile picture.

## Notes

- This tool only works with public, accessible profiles.
- For development and testing, mock data is used if real API access is not available.
- Respect privacy and terms of service when using this tool.

## License

MIT License

---

*Made with [LangChain](https://github.com/langchain-ai/langchain), Flask, and other great tools.*
