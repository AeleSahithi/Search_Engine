# Custom Search Engine with Exa API

## Overview

Imagine reading a funny tweet, and forgetting who tweeted it or where you saw it. Frustrating, right? Now, what if you could search for that exact content online in seconds? With **Natural Language Processing (NLP)** and **Large Language Models (LLMs)**, this is no longer a dream!

Here, we build a custom search engine that helps you rediscover content from the web using **Exa API**, an advanced API for semantic search. Unlike traditional search engines that rely on keyword matching, Exa uses LLMs to understand human language, providing more accurate and relevant results.

By the end of this guide, you'll have created a search engine that finds what you're thinking about, whether it's a tweet, a news article, or a web page. 

##  What is Exa API?

Exa (formerly **Metaphor**) is a powerful search API designed for semantic search. It leverages the latest NLP techniques and LLMs to retrieve high-quality and relevant content from the web. Exa allows you to search the web not just by keywords but by understanding the meaning behind your query.

With Exa, you can:
- Discover results based on the meaning of your query (semantic search)
- Search content from various domains (e.g., news, tweets, academic papers)
- Filter and customize results to get exactly what you need

## Setup and Installation

Before we dive into building our custom search engine, here’s what you need:

### Prerequisites

- Python 3.x installed on your system
- A **free Exa API key** (Get it [here](https://exa.ai/))
- `pip` (Python package installer) to install dependencies

## Installation

1. **Install the required Python packages**:

    ```bash
    pip install exa_py
    ```

2. **Ensure your API key for Exa is valid and added to the script**:

    ```python
    exa = Exa('your-api-key-here')
    ```


### Error Handling
- If the domains for news or Google search are invalid, ensure that they are provided in the correct format (e.g., `google.com` instead of `https://google.com`).
- If you encounter `ValueError: Invalid API Key`, verify that your Exa API key is correctly set.

