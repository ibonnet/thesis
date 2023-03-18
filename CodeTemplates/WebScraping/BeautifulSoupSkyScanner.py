import requests
from bs4 import BeautifulSoup

# Specify the URL of the website to scrape
url = 'https://www.skyscanner.com.ve/vuelos-desde/ve/vuelos-desde-venezuela.html'

# Send a GET request to the website and get the HTML content
response = requests.get(url)
html_content = response.content

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the flight information elements
flight_elements = soup.find_all('div', {'class': 'BpkTicket_bpk-ticket__3n-YG'})

# Loop through the flight elements and extract the necessary information
for flight_element in flight_elements:
    # Extract the airline name
    airline_name = flight_element.find('img')['alt']

    # Extract the flight number
    flight_number = flight_element.find('div', {'class': 'BpkTicket_bpk-ticket__flight-number__3i8Vw'}).get_text()

    # Extract the departure airport and time
    departure_airport = flight_element.find('div', {'class': 'BpkTicket_bpk-ticket__origin__1EP77'}).get_text()
    departure_time = flight_element.find('div', {'class': 'BpkTicket_bpk-ticket__departure-time__1B6pE'}).get_text()

    # Extract the arrival airport and time
    arrival_airport = flight_element.find('div', {'class': 'BpkTicket_bpk-ticket__destination__1yX9a'}).get_text()
    arrival_time = flight_element.find('div', {'class': 'BpkTicket_bpk-ticket__arrival-time__3XZW1'}).get_text()

    # Extract the price
    price = flight_element.find('div', {'class': 'BpkTicket_bpk-ticket__price__1Z-E5'}).get_text()

    # Print the flight information
    print(f'{airline_name} {flight_number} from {departure_airport} at {departure_time} to {arrival_airport} at {arrival_time} costs {price}')
