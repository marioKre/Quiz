import requests

# specifying parameters used for getting the questions data from API
parameters = {
    "amount": 10,
    "type": "boolean",
}
# set up GET request to API endpoint
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

# getting the data in JSON format, isolating results
data = response.json()
question_data = data["results"]
