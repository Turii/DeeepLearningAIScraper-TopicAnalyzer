# DeepLearning.AI Scraper & Topic Analyzer

This project was inspired by the [Building AI Browser Agents](https://learn.deeplearning.ai/courses/building-ai-browser-agents/) course by DeepLearning.AI. It includes a web scraping agent built with **Playwright** and a **data analytics pipeline** using both classical tools and a **local Mistral LLM** (via [Ollama](https://ollama.com)).

## Features

- Scrapes course titles, URLs, and descriptions from [deeplearning.ai/courses](https://www.deeplearning.ai/courses/)
- Performs frequency analysis and visualizations (bar chart + word cloud)
- Analyzes topics using a local Mistral language model
- Saves reports in separate folders for traditional and LLM-based analytics

## Setup

1. Install dependencies:
   
pip install -r requirements.txt

2. Run the scraper: python scrape_courses.py

3. Generate reports:

Traditional analysis: python analyze_topics.py
Mistral-based analysis: python analyze_with_mistral.py


You’ll need to install and run Ollama and pull the mistral model before LLM-based analysis:
ollama run mistral