import requests
import pandas as pd
from requests.exceptions import RequestException

def fetch_data(url):
    """
    Fetch data from API endpoint.
    Returns JSON data if successful, None if failed.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except RequestException as e:
        print(f"Network error occurred: {e}")
        return None

def create_dataframe(json_data):
    """
    Convert JSON data to pandas DataFrame.
    """
    return pd.DataFrame(json_data)

def save_to_excel(df, filename):
    """
    Save DataFrame to Excel file without index.
    """
    df.to_excel(filename, index=False)
    print(f"Data successfully saved to {filename}")

# Main execution
url = 'https://jsonplaceholder.typicode.com/todos'
data = fetch_data(url)

if data:
    # Convert to DataFrame
    df = create_dataframe(data)
    
    # Print the first few rows
    print(df.head())
    
    # Save to Excel
    save_to_excel(df, 'todos_data.xlsx')

# Count todos per user
user_task_counts = df['userId'].value_counts()

# Print the results
print(user_task_counts)
