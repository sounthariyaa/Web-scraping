import requests
from bs4 import BeautifulSoup

def scrape_postings():
    """
    This function scrapes the specified website and returns a list of the first 5 postings under the "Search Postings" heading.
    
    Returns:
    list: A list of dictionaries containing the Est. Value Notes, Description, and Closing Date fields for each posting.
    """
    try:
        # Send a GET request to the website
        url = "https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787"
        response = requests.get(url)
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find the "Search Postings" heading
        postings_heading = soup.find("h3", text="Search Postings")
        
        # Find the first 5 postings under the heading
        postings = []
        for posting in postings_heading.find_next_siblings("div")[:5]:
            # Extract the Est. Value Notes, Description, and Closing Date fields
            est_value_notes = posting.find("div", class_="est_value_notes").text.strip()
            description = posting.find("div", class_="description").text.strip()
            closing_date = posting.find("div", class_="closing_date").text.strip()
            
            # Add the fields to a dictionary and append it to the list of postings
            postings.append({
                "Est. Value Notes": est_value_notes,
                "Description": description,
                "Closing Date": closing_date
            })
        
        # Return the list of postings
        return postings
    except Exception as e:
        # Log the error
        print(f"Error: {e}")
        return []

# Required pip installs: requests, beautifulsoup4
