import pandas as pd
import bs4
from bs4 import BeautifulSoup as bs
import requests
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.71455000000003&lon=-74.00713999999994#.Xn9FbnUzYn4')
soup = bs(page.content, "html.parser")
# print(soup)
week = soup.find(id = 'seven-day-forecast-container')
# print(week)
items = soup.find_all(class_= 'forecast-tombstone')
# print(items)
# print(items[0])
periods = [item.find(class_ = 'period-name').get_text() for item in items ]
descriptions = [item.find(class_ = 'short-desc').get_text() for item in items]
tempratures = [item.find(class_ = 'temp').get_text() for item in items]
# print(periods)
# print(descriptions)
# print(tempratures)
weather_details = pd.DataFrame(
    {
        "period": periods,
        'description': descriptions,
        "temprature": tempratures
    }
)
print(weather_details)

weather_details.to_excel('weatherDetails.xls')