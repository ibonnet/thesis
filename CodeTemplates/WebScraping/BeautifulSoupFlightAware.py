import requests
from bs4 import BeautifulSoup

# Specify the URL of the website to scrape
url = 'https://flightaware.com/live/findflight?origin=SVMI&destination=&departure=&arrival=&airline=&flightno=&daterange=custom&startdate=01-01-2013&enddate=01-01-2023'

# Send a GET request to the website and get the HTML content
response = requests.get(url)
html_content = response.content

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the flight information elements
flight_elements = soup.find_all('tr', {'class': 'smallrow1'})

# Loop through the flight elements and extract the necessary information
for flight_element in flight_elements:
    # Extract the airline name and flight number
    airline_flight = flight_element.find('a', {'class': 'flightPageLink'}).get_text().strip()

    # Extract the departure airport and time
    departure_airport = flight_element.find('span', {'class': 'showAirportCode'}).get_text().strip()
    departure_time = flight_element.find('span', {'class': 'showLocalTime'}).get_text().strip()

    # Extract the arrival airport and time
    arrival_airport = flight_element.find_all('td')[3].get_text().strip()
    arrival_time = flight_element.find_all('td')[4].get_text().strip()

    # Extract the duration of the flight
    duration = flight_element.find_all('td')[5].get_text().strip()

    # Extract the status of the flight
    status = flight_element.find_all('td')[6].get_text().strip()

    # Print the flight information
    print(f'{airline_flight} from {departure_airport} at {departure_time} to {arrival_airport} at {arrival_time} ({duration}) - {status}')
