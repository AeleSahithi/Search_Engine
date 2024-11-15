# Search Engine Integration

This project provides a Python-based search engine that integrates APIs to retrieve data from various sources, including Google Search, news articles, and Twitter tweets. It uses the `exa_py` library for advanced querying and includes modular scripts for different search functionalities.

## Features
- **Google Search**: Fetch relevant results from Google and display key information such as titles and URLs.
- **News Search**: Retrieve articles from specific news domains like Google News and Hindustan Times.
- **Twitter Search**: Query Twitter to fetch tweets based on specific keywords or phrases.

## Technologies Used
- Python 3.11
- `exa_py` library for API integration
- Command-line input/output

## Setup Instructions

### Prerequisites
- Python 3.11 or later installed.
- An API key for the Exa API (replace in the script where necessary).
- Clone this repository:
  ```bash
  git clone https://github.com/AeleSahithi/Search_Engine.git
  cd Search_Engine

### Installation
1.**Install the required Python packages**:
 ```bash
pip install exa_py
 ```
2.**Ensure your API Key for Exa is valid and added to the script**:
 ```python
    exa = Exa('your-api-key-here')
    ``` 

