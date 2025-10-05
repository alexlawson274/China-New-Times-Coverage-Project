#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests


# In[4]:


from datetime import datetime
import time


# In[1]:


# --- Configuration ---
API_KEY = "KpkVzo0dmgT8uRm7e5MQUmlpXsdFVehe"
SEARCH_TERM = "BYD"
YEAR = 2023

# --- Function to query the NYT API ---
def count_nyt_articles(api_key, query, year):
    """
    Returns the number of New York Times articles for a given year that match the query.
    """
    # Define the date range for the entire year
    begin_date = f"{year}0101"
    end_date = f"{year}1231"

    # Construct the API URL
    base_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    params = {
        'api-key': api_key,
        'q': query,
        'begin_date': begin_date,
        'end_date': end_date,
        'facet_filter': 'true'
    }

    try:
        # Make the API request
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        # First, check if the API returned an error message
        if 'errors' in data:
            print(f"API returned an error: {data['errors']}")
            return 0

        # Check the overall status of the response
        status = data.get('status', 'ERROR').upper()
        if status != 'OK':
            print(f"API response status was not 'OK'. Status received: '{status}'")
            # Print additional error information if available
            if 'fault' in data:
                print(f"Fault details: {data['fault']}")
            return 0

        # Now safely try to get the hits count using safe dictionary access
        response_data = data.get('response', {})
        
        # Try both 'meta' and 'metadata' keys since we saw 'metadata' in the response
        meta_data = response_data.get('meta', {})
        if not meta_data:
            meta_data = response_data.get('metadata', {})
            
        total_hits = meta_data.get('hits')
        
        # Alternative: Check if hits is in the response directly
        if total_hits is None:
            total_hits = response_data.get('hits')

        if total_hits is not None:
            print(f"The query '{query}' appeared in approximately {total_hits} articles in {year}.")
            return total_hits
        else:
            print("Warning: 'hits' data not found in the API response.")
            print("Debug: Available keys in data:", data.keys())
            if 'response' in data:
                print("Debug: Available keys in response:", data['response'].keys())
                # Print the actual content of response for debugging
                print("Debug: Response content:", data['response'])
            return 0

    except requests.exceptions.RequestException as e:
        print(f"An error occurred with the API request: {e}")
        if 'response' in locals():
            print(f"HTTP Status Code: {response.status_code}")
            print(f"Response text: {response.text[:500]}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()

    return 0

# --- Execute the function ---
if __name__ == "__main__":
    count_nyt_articles(API_KEY, SEARCH_TERM, YEAR)


# In[25]:


import requests
import pandas as pd
from datetime import datetime
import time

# --- Configuration ---
API_KEY = "KpkVzo0dmgT8uRm7e5MQUmlpXsdFVehe"
YEAR = 2024

# List of countries to search for
countries = [
    "China",
    "Germany", 
    "India",
    "Japan",
    "Britain",
    "France",
    "Italy",
    "Canada",
    "Brazil",
    "Russia",
    "Spain",
    "South Korea",
    "Australia",
    "Mexico",
    "Indonesia",
    "Netherlands",
    "Saudi Arabia",
    "Poland",
    "Switzerland"
]
# --- Function to query the NYT API ---
def count_nyt_articles(api_key, query, year):
    """
    Returns the number of New York Times articles for a given year that match the query.
    """
    # Define the date range for the entire year
    begin_date = f"{year}0101"
    end_date = f"{year}1231"

    # Construct the API URL
    base_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    params = {
        'api-key': api_key,
        'q': query,
        'begin_date': begin_date,
        'end_date': end_date,
        'facet_filter': 'true'
    }

    try:
        # Make the API request
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        # First, check if the API returned an error message
        if 'errors' in data:
            print(f"API returned an error for '{query}': {data['errors']}")
            return 0

        # Check the overall status of the response
        status = data.get('status', 'ERROR').upper()
        if status != 'OK':
            print(f"API response status for '{query}' was not 'OK'. Status received: '{status}'")
            if 'fault' in data:
                print(f"Fault details: {data['fault']}")
            return 0

        # Now safely try to get the hits count using safe dictionary access
        response_data = data.get('response', {})
        
        # Try both 'meta' and 'metadata' keys since we saw 'metadata' in the response
        meta_data = response_data.get('meta', {})
        if not meta_data:
            meta_data = response_data.get('metadata', {})
            
        total_hits = meta_data.get('hits')
        
        # Alternative: Check if hits is in the response directly
        if total_hits is None:
            total_hits = response_data.get('hits')

        if total_hits is not None:
            return total_hits
        else:
            print(f"Warning: 'hits' data not found in the API response for '{query}'.")
            return 0

    except requests.exceptions.RequestException as e:
        print(f"An error occurred with the API request for '{query}': {e}")
        if 'response' in locals():
            print(f"HTTP Status Code: {response.status_code}")
    except Exception as e:
        print(f"An unexpected error occurred for '{query}': {e}")

    return 0

# --- Main execution with for loop ---
if __name__ == "__main__":
    print("Fetching NYT article counts for each country...")
    print("=" * 50)
    
    # Create a list to store results
    results = []
    
    for country in countries:
        print(f"Querying for: {country}")
        
        # Get the article count
        article_count = count_nyt_articles(API_KEY, country, YEAR)
        
        # Add to results
        results.append({
            'Country': country,
            'Year': YEAR,
            'NYT_Article_Count': article_count
        })
        
        # Print current result
        print(f"Result: {article_count} articles")
        print("-" * 30)
        
        # Important: Add delay to respect API rate limits (5 requests per minute)
        if country != countries[-1]:  # Don't sleep after the last request
            time.sleep(12)  # Sleep for 12 seconds between requests
    
    # Create a DataFrame table
    df = pd.DataFrame(results)
    
    print("\n" + "=" * 50)
    print("FINAL RESULTS TABLE:")
    print("=" * 50)
    print(df)
    
    # Optional: Display summary statistics
    print("\nSUMMARY:")
    print(f"Total articles across all countries: {df['NYT_Article_Count'].sum()}")
    print(f"Country with most coverage: {df.loc[df['NYT_Article_Count'].idxmax(), 'Country']} "
          f"({df['NYT_Article_Count'].max()} articles)")
    print(f"Average articles per country: {df['NYT_Article_Count'].mean():.1f}")


# In[26]:


df


# In[ ]:




