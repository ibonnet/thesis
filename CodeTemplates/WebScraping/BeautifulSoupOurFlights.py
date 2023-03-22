import requests
from bs4 import BeautifulSoup

# Specify the URL of the website to scrape
url = 'https://ourairports.com/airports/SVMI/flights.html'

# Send a GET request to the website and get the HTML content
response = requests.get(url)
html_content = response.content

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the flight information elements
flight_elements = soup.find_all('tr', {'class': 'timetable-record'})

# Loop through the flight elements and extract the necessary information
for flight_element in flight_elements:
    print (flight_element)
    
    # Extract the airline name and flight number
    airline_flight = flight_element.find('td', {'class': 'timetable-flight'}).get_text().strip()
    print (airline_flight)
    
    # Extract the arrival airport and time
    arrival_airport = flight_element.find_all('td', {'class': 'timetable-airport'}).get_text().strip()
    arrival_time = flight_element.find_all('td', {'class': 'timetable-time'}).get_text().strip()
    print (arrival_airport)
    print (arrival_time)
    
    # Extract the status
    arrival_status = flight_element.find_all('td', {'class': 'timetable-status'}).get_text().strip()
    print (arrival_status)
    
    # Print the flight information
    print(f'{airline_flight} to {arrival_airport} at {arrival_time} - {status}')
