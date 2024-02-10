import requests
import pandas as pd

def get_random_user_data():
    url = 'https://randomuser.me/api/'

    # Send a GET request to the API endpoint
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Normalize the JSON data into a pandas DataFrame
        df_results = pd.json_normalize(data["results"])

        # Selecting desired columns from the existing DataFrame
        new_df_results = df_results[['gender', 'name.first', 'name.last', 'location.city', 'location.state', 'location.country']].copy()

        # Return the new DataFrame
        return new_df_results
    else:
        print("Failed to retrieve data from the API")
        return None

# Call the function to get the DataFrame
random_user_data = get_random_user_data()

# Print the DataFrame (if available)
if random_user_data is not None:
    print(random_user_data)
