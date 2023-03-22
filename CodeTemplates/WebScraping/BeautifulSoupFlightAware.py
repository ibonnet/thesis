import requests
from bs4 import BeautifulSoup

# Specify the URL of the website to scrape
url = 'https://flightaware.com/live/airport/SVMI'

# Send a GET request to the website and get the HTML content
response = requests.get(url)
html_content = response.content

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the flight information elements
flight_elements = soup.find_all('tr', {'class': 'smallrow1'})

# Loop through the flight elements and extract the necessary information
for flight_element in flight_elements:
    print (flight_element)
    # Extract the airline name and flight number
    airline_flight = flight_element.find('td', {'class': 'flight-ident'}).get_text().strip()
    print (airline_flight)
    
    # Extract the departure airport and time
    departure_airport = flight_element.find('span', {'class': 'hint'}).get_text().strip()

    # Extract the arrival airport and time
    # arrival_airport = flight_element.find_all('td')[3].get_text().strip()
    # arrival_time = flight_element.find_all('td')[4].get_text().strip()
