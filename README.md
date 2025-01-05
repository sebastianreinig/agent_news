# Webpage Summarizer with OpenAI and Python

## Overview
This project is a Python-based application that fetches webpage content and subpage links, extracts their text, and generates summaries using OpenAI's API. It saves the summaries in a Markdown file, making it easier to process and analyze webpage content in a concise format.

The application leverages the `requests`, `BeautifulSoup`, and OpenAI libraries, along with environment variable management through `dotenv`.

## Requirements

To run this project, you'll need the following dependencies:

- `requests`
- `beautifulsoup4`
- `openai`
- `python-dotenv`

You can install these dependencies using:

```bash
pip install -r requirements.txt
```

## Setup and Usage

1. **Clone the Repository**  
   Clone this repository to your local machine.

2. **Environment Setup**  
   Create a `.env` file in the project root and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

3. **Input URLs**  
   Add URLs to a `urls.json` file in the following format:
   ```json
   {
       "urls": [
           "https://example.com",
           "https://another-example.com"
       ]
   }
   ```

4. **Run the Application**  
   Execute the script to fetch, summarize, and save content:
   ```bash
   python main.py
   ```

5. **Output**  
   The summaries will be saved to a Markdown file named `summaries_<date>.md`.

## Features

- **Webpage Content Extraction**  
  Fetches the main content from a webpage, including paragraphs (`<p>` tags).
  
- **Subpage Link Crawling**  
  Identifies and processes subpage links within the main page.

- **Text Summarization**  
  Uses OpenAI's API to generate concise summaries of the content.

- **Markdown Export**  
  Saves all summaries in a well-structured Markdown file for easy review.

## How It Works

1. **Environment Variable Management**  
   The `.env` file is used to securely store and retrieve the OpenAI API key.

2. **Webpage and Subpage Processing**  
   The application fetches both the main page and its subpages, extracting their textual content.

3. **OpenAI Summarization**  
   The combined text is sent to OpenAI's API, which returns a summary.

4. **Output**  
   Summaries are written to a Markdown file, categorized by URL.

## Example

Here's an example output saved in the Markdown file:

```markdown
# Summaries

## https://example.com

This webpage discusses the benefits of using Python for web development, including its simplicity and robust libraries.

## https://example.com/about

The 'About' page explains the company's history, mission, and core values.
```

## Future Enhancements

- Add support for fetching metadata like titles and descriptions.
- Improve subpage filtering to avoid irrelevant links.
- Introduce error handling for complex webpage structures.

## Disclaimer
Important: Always ensure you have the right to scrape and process content from any webpage. Many websites prohibit web scraping in their terms of service. Before using this tool, review the website’s terms and conditions and obtain explicit permission if necessary. Unauthorized scraping of websites may violate legal or ethical standards and can lead to penalties or legal action. Use this tool responsibly and in compliance with applicable laws and regulations.


## Credits

This project was created using:

- Python
- BeautifulSoup for HTML parsing
- OpenAI API for text summarization

Feel free to contribute, suggest improvements, or report issues in the repository.
