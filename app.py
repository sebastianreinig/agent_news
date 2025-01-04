import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import datetime
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


def fetch_webpage_text(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        # Extract the main content of the webpage
        paragraphs = soup.find_all("p")
        text = "\n".join(p.get_text() for p in paragraphs)
        return text
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        return None

def fetch_subpage_links(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        links = set()
        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            if href.startswith("/") or href.startswith(url):
                full_url = href if href.startswith("http") else requests.compat.urljoin(url, href)
                links.add(full_url)
        return links
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch subpage links from {url}: {e}")
        return set()

def summarize_text_with_openai(text, openai_client):
    try:
        completion = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes texts."},
                {"role": "user", "content": f"Please summarize the following text:\n{text}"}
            ]
        )
        return completion.choices[0].message['content']
    except Exception as e:
        print(f"Failed to summarize text: {e}")
        return None

def save_summaries_to_file(summaries):
    date_str = datetime.date.today().isoformat()
    filename = f"summaries_{date_str}.md"
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("# Summaries\n\n")
            for url, summary in summaries.items():
                file.write(f"## {url}\n\n")
                file.write(f"{summary}\n\n")
        print(f"Summaries saved to {filename}")
    except IOError as e:
        print(f"Failed to save summaries: {e}")

def main():
    # List of URLs to summarize
    urls = [
        "https://example.com",
        "https://example.org",
        "https://example.net"
    ]

    # Initialize OpenAI client with API key
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        print("OpenAI API key not found. Please set it in the .env file.")
        return

    openai_client = OpenAI(api_key=openai_api_key)

    summaries = {}

    for url in urls:
        print(f"Processing {url}...")
        main_text = fetch_webpage_text(url)
        if main_text:
            print("Fetched main page text.")

        subpage_links = fetch_subpage_links(url)
        subpage_texts = []
        for subpage_url in subpage_links:
            print(f"Fetching subpage {subpage_url}...")
            subpage_text = fetch_webpage_text(subpage_url)
            if subpage_text:
                subpage_texts.append(subpage_text)

        combined_text = (main_text or "") + "\n" + "\n".join(subpage_texts)

        if combined_text.strip():
            print("Summarizing combined text...")
            summary = summarize_text_with_openai(combined_text, openai_client)
            if summary:
                summaries[url] = summary
                print(f"Summary for {url}:\n{summary}\n")
            else:
                print(f"Failed to summarize the content of {url}.")
        else:
            print(f"No content to summarize for {url}.")

    if summaries:
        save_summaries_to_file(summaries)

if __name__ == "__main__":
    main()
