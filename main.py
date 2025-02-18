import json
from scraper.glossary_scraper import GlossaryScraper

def main():
    """Scrape the CC Wiki glossary and print the results as JSON."""
    url = "https://cc-wiki.cdq.com/Glossary" 
    scraper = GlossaryScraper()
    scraper.fetch_page(url)
    glossary_data = scraper.extract_content()

    print("Finished scraping and building the ontology. Check glossary.owl.")

    # Pretty-print as JSON
    print(json.dumps(glossary_data, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
