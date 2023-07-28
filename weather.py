import requests
import json

def showWeather(city):
    # api key here
    api_key = "53049bc3c15db71fff12be30a52c2dc3"
    Response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}"
    )
    # json method of response object
    # convert json format data into
    # python format data
    x = Response.json()
 
    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to 200
    # "401", means city is found otherwise
    # city is not found
    if x['cod'] == 200:
        kelvin = 401
    
        # store the value of "main"
        # key in variable y
        y = x["main"]
    
        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]
        # print following values
        print(" The tempreture in " + city + " " + "is" + " " + str(current_temperature) +"°C" )
    
    else:
        print(" Invalid data or error in fetching data ")
    
def inp():
    #getting city name from user
    city_name = input("Enter the city name :")
    showWeather(city_name)
inp()