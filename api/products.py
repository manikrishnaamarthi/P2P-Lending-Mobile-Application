import requests

class P2PApi:
    def __init__(self, base_url):
        self.base_url = base_url

    def initiate_transaction(self, data):
        # Example API endpoint for initiating P2P transaction
        endpoint = "/transactions/initiate"
        url = f"{self.base_url}{endpoint}"

        # Make a POST request to the API endpoint
        response = requests.post(url, json=data)

        # Check if the request was successful
        if response.status_code == 200:
            return response.json()
        else:
            # Handle errors or raise an exception
            response.raise_for_status()

# Add more methods or classes for additional API endpoints as needed
