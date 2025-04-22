import requests
import pandas as pd
from requests.exceptions import RequestException

try:
    # Define the API URL
    url = 'https://jsonplaceholder.typicode.com/todos'
    
    # Make GET request to the URL
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON data
        json_data = response.json()
        
        # Convert JSON to DataFrame
        df = pd.DataFrame(json_data)
        
        # Print the first few rows
        print(df.head())
        
        # Save to Excel
        df.to_excel('todos_data.xlsx', index=False)
        
        # Print success message
        print("Data successfully saved to todos_data.xlsx")
    else:
        print(f"Error: Received status code {response.status_code}")
        exit()
        
except RequestException as e:
    print(f"Network error occurred: {e}")
