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


# Initialize an empty DataFrame to store all the results
all_results = pd.DataFrame()


# Call the function to get the DataFrame
i = 0
while i<100 :
  random_user_data = get_random_user_data()
  all_results = pd.concat([all_results, random_user_data], ignore_index=True)  # Concatenate current data to all_results
  i += 1

# Print the combined DataFrame
print(all_results)
